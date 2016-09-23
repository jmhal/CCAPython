from gov.cca import Port

class GoPort(Port):
   def __init__(self):
      super(GoPort, self).__init__("gov.cca.ports.GoPort")
      return
   
   def go(self):
      """
      input: none
      output: a integer. 0 for Ok, -1 for troubles but still can go on, -2 for fatal error
      """
      raise NotImplementedError("Abstract Class!")  

class BuilderService(Port):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")  

   def createInstance(self, instanceName, className, properties):
      """
      input: a string instanceName, a string className, a gov.ccaTypeMap properties
      output: a gov.cca.ComponentID object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getDeserialization(self, s):
      """
      input: a string s
      output: a gov.cca.ComponentID object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def connect(self, user, usingPortName, provider, providingPortName):
      """
      input: a gov.cca.ComponentID object user, a string usingPortName, a gov.cca.ComponentID object provider, a string providingPortName
      output: a gov.cca.ConnectionID object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def disconnect(self, connID, timeout):
      """
      input: a gov.cca.ConnectionID object connID, a float timeout
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def disconnectAll(self, id1, id2, timeout):
      """
      input: a gov.cca.ComponentID id1, a gov.cca.ComponentID id2, a float timeout
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def destroyInstance(self, toDie, timeout):
      """
      input: a gov.cca.ComponentID toDie, a float timeout
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getComponentProperties(self, cid):
      """
      input: a gov.cca.ComponentID cid
      output: a gov.cca.TypeMap
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def setComponentProperties(self, cid, properties):
      """
      input: a gov.cca.ComponentID cid, a gov.cca.TypeMap properties
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getPortProperties(self, cid, portName):
      """
      input: a gov.cca.ComponentID cid, a string portName
      output: a gov.cca.TypeMap
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def setPortProperties(self, cid, portName, properties):
      """
      input: a gov.cca.ComponentID cid, a string portName, a gov.cca.TypeMap properties
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getConnectionProperties(self, connID):
      """
      input: a gov.cca.ConnectionID connID
      output: a gov.cca.TypeMap
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def setConnectionProperties(self, connID, properties):
      """
      input: a gov.cca.ConnectionID connID, a gov.cca.TypeMap properties
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  
 
   def getComponentID(self, componentInstanceName):
      """
      input: a string componentInstanceName
      output: a gov.cca.ComponentID
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getComponentIDs(self):
      """
      input: none
      output: a list of gov.cca.ComponentID
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getProvidedPortNames(self, cid):
      """
      input: a gov.cca.ComponenID cid
      output: a list of strings
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getUsedPortNames(self, cid):
      """
      input: a gov.cca.ComponenID cid
      output: a list of strings
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

   def getConnectionIDs(self, componentList):
      """
      input: a list of gov.cca.ComponentID
      output: a list of goc.cca.ConnectionID
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")  

class EventType():
   Error = -1
   ALL = 0
   ConnectPending = 1
   Connected = 2
   DisconnectPending = 3
   Disconnected = 4
   def __init__(self):
      raise NotImplementedError("Enumeration!")
   
class ConnectionEvent(Port):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")  
 
   def getEventType(self):
      """
      input: none
      output: a EventType object
      """
      raise NotImplementedError("Abstract Class!")  

   def getPortInfo(self):
      """
      input: none
      output: a gov.cca.TypeMap object  
      """
      raise NotImplementedError("Abstract Class!")  

class ConnectionEventListener(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")  

   def connectionActivity(self, ce):
      """
      input: a gov.cca.ports.ConnectionEvent ce
      output: void
      """
      raise NotImplementedError("Abstract Class!")  

class ConnectionEventService(Port):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")  

   def addConnectionEventListener(self, et, cel):
      """
      input: a gov.cca.ports.EventType et, a gov.cca.ports.ConnectionEventListener cel
      output: void
      """
      raise NotImplementedError("Abstract Class!")  
 
   def removeConnectionEventListener(self, et, cel):
      """
      input: a gov.cca.ports.EventType et, a gov.cca.ports.ConnectionEventListener cel
      output: void
      """
      raise NotImplementedError("Abstract Class!")

class ComponentRepository(Port):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def getAvailableComponentClasses(self):
      """
      input: none
      output: a list of gov.cca.ComponentClassDescription
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

class ServiceProvider(Port):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def createService(self, portType):
      """
      input: a string portType
      output: a string with the name of the port
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def destroyService(self, portName):
      """
      input: a string portName
      output: none
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

class ServiceRegistry(Port):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def addService(self, serviceType, portProvider):
      """
      input: a string serviceType, a gov.cca.ports.ServiceProvider object portProvider
      output: a boolean
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def addSingletonService(self, serviceType, server):
      """
      input: a string serviceType, a gov.cca.Port object server
      output: a boolean
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def removeService(self, serviceType):
      """
      input: a string serviceType
      output: none
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")



