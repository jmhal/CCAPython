from gov.cca import Services
from gov.cca.ports import ConnectionEventService
from framework.info.connectioninfo import ConnectionEvent
from framework.common.typemap import TypeMapDict
from framework.common.exceptions import PortNotFoundException

class ServicesHandle(Services, ConnectionEventService):
   def __init__(self):
      # Maps strings portName to a tuple (gov.cca.Ports, gov.cca.TypeMap).
      # (portName) -> (Port, TypeMap)
      self.d_usesports = {}
      self.d_providesports = {}
    
      # Maps string ports names to string ports types
      # (portName) -> (portType)
      self.d_portType = {}

      # Maps a gov.cca.ports.EventType to a list of gov.cca.ports.EventListener
      # (EventType) -> (ConnectionEventListener [])
      self.d_listeners = {}

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
      pass
   
   def setInstanceProperties(self, properties):
      """
      input: a gov.cca.TypeMap properties
      output: none
      """
      pass

   def setPortProperties(self, portName, properties):
      """
      input: a string portName, a gov.cca.TypeMap properties
      output: none
      """
      pass

   def getProvidedPortNames(self):
      """
      input: none
      output: a list of strings
      """
      

   def getUsedPortNames(self):
      """
      input: none
      output: a list of strings
      """
      pass

   def bindPort(self, portName, port):
      """
      input: a string portName, a gov.cca.Port object
      output: void
      """
      if portName not in d_usesports.keys():
         raise PortNotFoundException(portName)
      d_usesports[portName] = (port, TypeMapDict())
      return

   def getProvidesPort(self, name):
      """
      input: string name
      output: void
      """
      if name not in self.d_providesports.keys():
         raise PortNotFoundException(name) 
      return d_providesports[name][TypeMapDict()]
         
   def notifyConnectionEvent(self, portName, event):
      """
      This method will notify the component from the calling Services of an event
      input: string portName, a gov.cca.ports.EventType event)
      output: void
      """
      listenerList = [] 
      for ev in d_listeners.keys():
         if ev == event:
            listenerList += d_listeners[event]
       
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
      pass

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
      pass

   def getPortNonblocking(self, portName):
      """
      input: string portName
      output: a Port object
      throws CCAException
      """
      pass

   def releasePort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      pass
 
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


