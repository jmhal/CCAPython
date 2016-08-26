from gov.cca import AbstractFramework
from gov.cca.ports import BuilderService

class Builder(AbstractFramework, BuilderService):
   def __init__(self):
      pass

   # New Methods
   def lookupPort(self, componentID, portName):
      """
      Simplifies the access to GoPort on components without requiring the main method to register itself with
      a gov.cca.Services object.
      input: gov.cca.ComponentID componentID, string portName
      output: a gov.cca.Port object
      """
      pass
  
   def provideRequestedServices(self, componentID, portName, portType)
      """
      Provides access to two ports implemented by the framework itself: BuilderService and ConnectionEventService
      input: a gov.cca.ComponentID object, a string portName, a string portType
      output: void
      """
      pass

   # Methods from AbstractFramework
   def createTypeMap(self):
      """
      input: none 
      output: a TypeMap object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def createEmptyFramework(self):
      """
      input: none 
      output: a AbstractFramework object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def getServices(self, selfInstanceName, selfClassName, selfProperties):
      """
      input: a string selfInstanceName, string selfClassName, TypeMap selfProperties
      output: a Services object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def releaseServices(self, services):
      """
      input: a Services object
      output: a AbstractFramework object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def shutdownFramework(self):
      """
      input: none
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")
  
   # Methods from BuilderService
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


