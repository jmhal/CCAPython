from gov.cca import Services
from gov.cca.ports import ConnectionEventService
from framework.info.connectioninfo import ConnectionEvent
from framework.common.typemap import TypeMapDict
from framework.common.exceptions import PortNotFoundException

class ServicesHandle(Services, ConnectionEventService):
   def __init__(self):
      # Maps strings portName to a tuple (gov.cca.Ports, gov.cca.TypeMap).
      # (portName) -> (Port, TypeMap)
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
      if portName in self.d_providesPort:
         self.d_providesPort[portName][1] = properties
      else if portName in self.d_usesPort:
         self.d_usesPort[portName][1] = properties
      else:
         raise PortNotFoundException(portName)

   def getProvidedPortNames(self):
      """
      input: none
      output: a list of strings
      """
      return self.d_providesPort.keys()
      
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
      self.d_usesPort[portName] = (port, TypeMapDict())
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
      tm.putString("cca.PortType", d_portType[portName])
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
      pass

   def createTypeMap(self):
      """
      input: none
      output: a TypeMap object
      throws CCAException
      """
      return TypeMapDict() 

   def registerUsesPort(self, portName, type, properties):
      """
      input: string portName, string type, and TypeMap properties
      output: void
      throws CCAException
      """
      pass
  
   def unregisterUsesPort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      pass
 
   def addProvidesPort(self, inPort, portName, type, properties):
      """
      input: Port inPort, string portName, string type, and TypeMap properties
      output: void
      throws CCAException
      """
      pass
  
   def removeProvidesPort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      pass

   def getPortProperties(self, portName):  
      """
      input: string portName
      output: a TypeMap object 
      """
      pass

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
      pass 

   # Methods from gov.cca.ports.ServiceRegistry
   def addService(self, serviceType, portProvider):
      """
      input: a string serviceType, a gov.cca.ports.ServiceProvider object portProvider
      output: a boolean
      throws CCAException
      """
      pass

   def addSingletonService(self, serviceType, server):
      """
      input: a string serviceType, a gov.cca.Port object server
      output: a boolean
      throws CCAException
      """
      pass

   def removeService(self, serviceType):
      """
      input: a string serviceType
      output: none
      throws CCAException
      """
      pass

   # Methods from gov.cca.ports.ConnectionEventService
   def addConnectionEventListener(self, et, cel):
      """
      input: a gov.cca.ports.EventType et, a gov.cca.ports.ConnectionEventListener cel
      output: void
      """
      pass  
 
   def removeConnectionEventListener(self, et, cel):
      """
      input: a gov.cca.ports.EventType et, a gov.cca.ports.ConnectionEventListener cel
      output: void
      """
      pass


