from gov.cca import Services
from gov.cca.ports import ConnectionEventService

class ServiceHandle(Services, ConnectionEventService):
   def __init__(self):
      # Maps strings port names do gov.cca.Ports objects and gov.cca.TypeMap properties objects.
      self.d_usesports = {}
      self.d_providesports = {}
    
      # Maps a gov.cca.ports.EventType to a list of gov.cca.ports.EventListeners
      self.d_listeners = {}

   # New methods
   def initialize(self, fwk, componentID, properties):
      """
      input: a gov.cca.AbstractFramework fwk, a gov.cca.ComponentID componentID and a gov.cca.TypeMap properties
      ouput: void
      """
      self.framework = fwk
      self.componentID = componentID
      self.properties = properties
  
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

   def getProviderPortNames(self):
      """
      input: none
      output: a list of strings
      """
      pass

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
      pass

   def getProvidesPort(self, name):
      """
      input: string name
      output: void
      """
      pass

   def notifyConnectionEvent(self, portName, event):
      """
      input: string portName, a gov.cca.ports.EventType event)
      output: void
      """
      pass

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


