from gov.cca import Services
from gov.cca.ports import ConnectionEventService
from gov.cca.ports import EventType
from framework.info.connectioninfo import ConnectionEvent
from framework.common.typemap import TypeMapDict
from framework.common.exceptions import PortNotFoundException

class ServicesHandle(Services, ConnectionEventService):
   def __init__(self):
      # Maps strings portName to a list (gov.cca.Ports, gov.cca.TypeMap).
      # (portName) -> [Port, TypeMap]
      self.d_usesPort = {}
      self.d_providesPorts = {}
    
      # Maps string ports names to string ports types
      # (portName) -> (portType)
      self.d_portType = {}

      # Maps a gov.cca.ports.EventType value to a list of gov.cca.ports.EventListener
      # (EventType) -> (ConnectionEventListener [])
      self.d_listeners = {}

      # A gov.cca.Type containing the properties of the component instance
      self.d_instanceProperties = TypeMapDict()

   # New methods
   def initialize(self, fwk, componentID, properties, is_alias):
      """
      input: a gov.cca.AbstractFramework fwk, a gov.cca.ComponentID componentID and a gov.cca.TypeMap properties
      ouput: void
      """
      self.framework = fwk
      self.componentID = componentID
      self.properties = properties
      self.d_is_alias = is_alias
  
   def getInstanceProperties():
      """
      input: none
      output: a gov.cca.TypeMap object
      """
      return self.d_instanceProperties 
   
   def setInstanceProperties(self, properties):
      """
      input: a gov.cca.TypeMap properties
      output: none
      """
      self.d_instanceProperties = properties
      return

   def setPortProperties(self, portName, properties):
      """
      input: a string portName, a gov.cca.TypeMap properties
      output: none
      """
      if portName in self.d_providesPorts:
         elf.d_providesPorts[portName][1] = properties
      elif portName in self.d_usesPort:
         self.d_usesPort[portName][1] = properties
      else:
         raise PortNotFoundException(portName)

   def getProvidedPortNames(self):
      """
      input: none
      output: a list of strings
      """
      return self.d_providesPorts.keys()
      
   def getUsedPortNames(self):
      """
      input: none
      output: a list of strings
      """
      return self.d_usesPort.keys()

   def bindPort(self, portName, port):
      """
      input: a string portName, a gov.cca.Port object
      output: void
      """
      if portName not in self.d_usesPort.keys():
         raise PortNotFoundException(portName)
      self.d_usesPort[portName] = [port, TypeMapDict()]
      return

   def getProvidesPort(self, name):
      """
      input: string name
      output: void
      """
      if name not in self.d_providesPorts.keys():
         raise PortNotFoundException(name) 
      return self.d_providesPorts[name][0]
         
   def notifyConnectionEvent(self, portName, event):
      """
      This method will notify the component from the calling Services of an event
      input: string portName, a gov.cca.ports.EventType value event
      output: void
      """
      listenerList = [] 
      for ev in self.d_listeners:
         if ev == event:
            listenerList += self.d_listeners[event]
       
      tm = TypeMapDict()
      tm.putString("cca.PortName", portName)
      tm.putString("cca.PortType", self.d_portType[portName])
      ce = ConnectionEvent(event, tm) 
      for listener in listenerList:
         listener.connectionActivity(ce)
      return

   # Methods from gov.cca.Services
   def getComponentID(self):
      """
      input: none
      output: a ComponentID object
      """
      return self.componentID 

   def createTypeMap(self):
      """
      input: none
      output: a TypeMap object
      throws CCAException
      """
      return TypeMapDict() 

   def registerUsesPort(self, portName, _type, properties):
      """
      input: string portName, string type, and TypeMap properties
      output: void
      throws CCAException
      """
      if portName in self.d_providesPorts or portName in self.d_usesPort:
         print portName + " is not unique. Not doing anything."
         return 
      else:
         self.d_usesPort[portName] = [None, properties]
         self.d_portType[portName] = _type
         if self.framework != None:
            if self.framework.isProvidedService(_type):
               self.framework.provideRequestedServices(self.d_componentID, portName, _type) 
 
   def unregisterUsesPort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      self.d_usesPort.pop(portName, None)
      self.d_portType.pop(portName, None)
      return 

   def addProvidesPort(self, inPort, portName, _type, properties):
      """
      input: Port inPort, string portName, string type, and TypeMap properties
      output: void
      throws CCAException
      """
      if portName in self.d_providesPorts or portName in self.d_usesPort:
         print portName + " is not unique. Not doing anything."
         return 
      if not self.d_is_alias and not inPort.isType(_type):
         print "Port instance is not an instance of specified type"
         return
      self.d_providesPorts[portName] = [inPort, properties]
      self.d_portType[portName] = _type
      return
  
   def removeProvidesPort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      self.d_providesPorts.pop(portName, None)
      self.d_portType.pop(portName, None)
      return 

   def getPortProperties(self, portName):  
      """
      input: string portName
      output: a TypeMap object 
      """
      if portName in self.d_usesPort:
         return self.d_usesPort[portName][1]
      elif portName in self.d_providesPorts:
         return self.d_providesPorts[portName][1]
      else :
         return None

   def getPort(self, portName):
      """
      input: string portName
      output: a Port object
      throws CCAException
      """
      if portName in self.d_usesPort:
         return self.d_usesPort[portName][0]

   def getPortNonblocking(self, portName):
      """
      input: string portName
      output: a Port object
      throws CCAException
      """
      return self.getPort(portName)

   def releasePort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      if portName in self.d_usesPort:
         self.d_usesPort[portName] = None
 
   def registerForRelease(self, callback):
      """
      input: a gov.cca.ComponentRelease object callback
      output: void
      """
      self.framework.setInstanceRelease(self.componentID, callback)

   # Methods from gov.cca.ports.ServiceRegistry
   def addService(self, serviceType, portProvider):
      """
      input: a string serviceType, a gov.cca.ports.ServiceProvider object portProvider
      output: a boolean
      throws CCAException
      """
      self.framework.addServiceProvider(serviceType, self.componentID, portProvider)
      return True

   def addSingletonService(self, serviceType, server):
      """
      input: a string serviceType, a gov.cca.Port object server
      output: a boolean
      throws CCAException
      """
      self.framework.addServicePort(serviceType, server)
      return true

   def removeService(self, serviceType):
      """
      input: a string serviceType
      output: none
      throws CCAException
      """
      self.framework.removeFromRegistry(serviceType)
      return None

   # Methods from gov.cca.ports.ConnectionEventService
   def addConnectionEventListener(self, et, cel):
      """
      input: a gov.cca.ports.EventType et, a gov.cca.ports.ConnectionEventListener cel
      output: void
      """
      if et == EventType.Error:
         return 
      if et == EventType.ALL:
         self.addConnectionEventListener(EventType.ConnectPending)
         self.addConnectionEventListener(EventType.Connected)
         self.addConnectionEventListener(EventType.DisconnectPending)
         self.addConnectionEventListener(EventType.Disconnected)
      elif cel not in self.d_listeners[et]:
         self.d_listeners[et].append(cel) 
         return

   def removeConnectionEventListener(self, et, cel):
      """
      input: a gov.cca.ports.EventType et, a gov.cca.ports.ConnectionEventListener cel
      output: void
      """
      if et == EventType.Error:
         return 
      if et == EventType.ALL:
         for event in self.d_listeners:
             self.removeConnectionEventListener(event, cel)
         return
      else:
         self.d_listeners[et].remove(cel) 
         return

      

