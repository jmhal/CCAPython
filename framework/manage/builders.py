import uuid

from gov.cca import AbstractFramework
from gov.cca import Port
from gov.cca.ports import BuilderService
from gov.cca.ports import EventType
from framework.info.connectioninfo import ConnectionID
from framework.info.componentinfo import ComponentID
from framework.common.exceptions import InstanceNotFoundException
from framework.manage.services import ServicesHandle

class ProviderEntry():
   def __init__(self, componentID, serviceProvider):
      self.componentID = componentID
      self.serviceProvider = serviceProvider
      return

class ComponentInstance():
   def __init__(self, component, services):
      self.component = component
      self.services = services

      # Maps a string port name to a gov.cca.ConnectionID
      self.usesConnection = {}

      # Maps a string port name to a set of gov.cca.ConnectionID
      # Has to be initialized with every provides port from the component
      # I'm considering that each component has only one connection to another component through the same uses/provides port.
      self.providesConnection = {}
      
class FrameworkHandle(AbstractFramework, BuilderService):
   def __init__(self):
      # Maps a string corresponding to a component instance name a ComponentInstance object
      # (instanceName) -> (ComponentInstance)
      self.d_instance = {}

      # (string portType) -> (ProviderEntry)
      self.d_serviceProviders = {}

      # (string portType) -> (gov.cca.Port)
      self.d_servicePorts = []

      # Maps instance names to class names
      # (instanceName) -> (className)   
      self.d_aliases = {}

   # New Methods
   def lookupPort(self, componentID, portName):
      """
      Simplifies the access to GoPort on components without requiring the main method to register itself with
      a gov.cca.Services object.
      input: gov.cca.ComponentID componentID, string portName
      output: a gov.cca.Port object
      """
      instanceName = componentID.getInstanceName() 
      if instanceName not it self.d_instance.keys():
         raise InstanceNotFound(instanceName)
      return self.d_instance[instanceName].services.getProvidesPort(portName)

   def isProvidedService(self, portType):
      """
      input: a string portType
      output: a boolean
      """
      if portType == "gov.cca.ports.ConnectionEventService" or portType == "gov.cca.ports.ServiceRegistry" :
         return True
      if portType in self.d_serviceProviders.keys() or portType in self.d_servicePorts.keys():
         return True
      return False

   def provideRequestedServices(self, componentID, portName, portType)
      """
      Provides access to two ports implemented by the framework itself: BuilderService and ConnectionEventService
      input: a gov.cca.ComponentID object, a string portName, a string portType
      output: void
      """
      if portType == "gov.cca.ports.ConnectionEventService" : 
         userSvcs = self.d_instance[componentID.getInstanceName()].services
         uniqueName = getUniqueName("connectionEventer")
         svcs = getServices(uniqueName, portType, 0)
         svcs.addProvidesPort(userSvcs, "ConnectionEventService", portType, 0)
         connect(componentID, portName, svcs.getComponentID(), "ConnectionEventService")
      else if portType == "gov.cca.ports.ServiceRegistry" :
         userSvcs = self.d_instance[componentID.getInstanceName()].services
         uniqueName = getUniqueName("registryService")
         svcs = getServices(uniqueName, portType, 0)
         svcs.addProvidesPort(userSvcs, "RegistryService", portType, 0)
         connect(componentID, portName, svcs.getComponentID(), "RegistryService")
      else if portType in self.d_servicePorts.keys() :
         port = self.d_servicePorts[portType]
         uniqueName = getUniqueName("singletonPort")
         svcs = getServices(uniqueName, portType, 0)
         svcs.addProvidesPort(port, "AvailService", portType, 0)
         connect(componentID, portName, svcs.getComponentID(), "AvailService")
      else if portType in self.d_serviceProviders.keys() :
         pe = d_servicesProviders[portType]
         sp = pe.serviceProvider
         portName = sp.createService(portType) 
         connect(componentID, portName, pe.componentID, portName)
      return

   def addServiceProvider(self, portType, componentID, provider):
      """
      input: a string portType, a gov.cca.ComponenteID componentID, a gov.cca.ports.ServiceProvider provider
      output: none
      """
      pass

   def addServicePort(self, portType, port):
      """
      input: a string portType, gov.cca.Ports port
      output: none
      """
      pass

   def removeFromRegistry(self, portType):
      """
      input: a string portType
      output: none
      """
      pass

   def setInstanceRelease(self, componentID, callback):   
      """
      input: a gov.cca.ComponentID componentID, a gov.cca.ComponentRelease callback2 
      output: none
      """
      pass

   def getUniqueName(self, requestedName):
      """
      input: a string requestedName
      output: a string that is unique in the framework scope
      """
      return requestedName + "::" + str(uuid.uuid4())

   def removeInstance(self, instanceName):
      """
      input: a string instanceName
      output: a integer
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
      nil = None
      cid = ComponentID(None)
      uniqueName = getUniqueName(selfInstanceName)
      cid.initialize(uniqueName)
      svcs = ServicesHandle()
      svcs.initialize(self, cid, selfProperties) 
      self.d_instance[uniqueName].component = nil;
      self.d_instance[uniqueName].svcs = svcs
      self.d_aliases[uniqueName] = selfClassName
      return svcs

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
      connectionID = ConnectionID()
      userName = user.getInstanceName()
      provName = provider.getInstanceName()
      if (userName not it d_instance.keys()) and (provName not it d_instance.keys()) :
         userSvc = d_instance[userName].services
         provSvc = d_instance[provName].services

         provSvc.notifyConnectionEvent(provindingPortName, EventType.ConnectPending)
         userSvc.notifyConnectionEvent(usingPortName, EventType.ConnectPending)

         port = provSvc.getProvidesPort(providingPortName)   
         
         userSvc.bindPort(usingPortName, Port)
         connectID = ConnectionID()
         connectID.initialize(provider, providingPortName, user, usingPortName, 0)

         d_instance[userName].usesConnection[usingPortName] = connectID
         d_instance[provName].providesConnection[provindingPortName].append(connectID)

         provSvc.notifyConnectionEvent(providingPortName, EventType.Connected)
         usesSvc.notifyConnectionEvent(usingPortName, EventType.Connected)
    return connectionID


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


