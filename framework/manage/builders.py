import uuid
import importlib

from gov.cca import AbstractFramework
from gov.cca import Port
from gov.cca.ports import BuilderService
from gov.cca.ports import EventType
from framework.info.connectioninfo import ConnectionID
from framework.info.componentinfo import ComponentID
from framework.common.exceptions import InstanceNotFoundException
from framework.manage.services import ServicesHandle
from framework.common.typemap import TypeMapDict

class ProviderEntry():
   def __init__(self, componentID, serviceProvider):
      self.componentID = componentID
      self.serviceProvider = serviceProvider
      return

class ComponentInstance():
   def __init__(self, component, release, services):
      self.component = component
      self.release = release
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
      pe = ProviderEntry(componentID, provider)
      self.d_serviceProviders[portType] = pe
      return

   def addServicePort(self, portType, port):
      """
      input: a string portType, gov.cca.Ports port
      output: none
      """
      self.d_servicePorts[portType] = port
      return 

   def removeFromRegistry(self, portType):
      """
      input: a string portType
      output: none
      """
      if portType != "gov.cca.ports.BuilderService":
         self.d_servicePorts.pop(portType, None)
         self.d_serviceProviders.pop(portType, None
      return 

   def setInstanceRelease(self, componentID, callback):   
      """
      input: a gov.cca.ComponentID componentID, a gov.cca.ComponentRelease callback2 
      output: none
      """
      instanceName = componentID.getInstanceName()
      self.d_instance[instanceName].release = callback
      return

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
      if instanceName not in self.d_instance.keys():
         return 0
       
      connectionIDs = []

      # Collect all connection IDs
      for connection in self.d_instance[instanceName].usesConnection:
         connectionIDs.append(self.d_instance[instanceName].usesConnection[connection])

      # Destroy all connections
      for id_ in connectionIDs:
         disconnect(id_, 0.0)
       
      # Remove the instance itself
      instance = self.d_instance[instanceName]
      instance.release.releaseServices(instance.services)
      self.d_instance.pop(instanceName, None)
   
      return 1

   # Methods from AbstractFramework
   def createTypeMap(self):
      """
      input: none 
      output: a TypeMap object
      throws CCAException
      """
      return TypeMapDict() 

   def createEmptyFramework(self):
      """
      input: none 
      output: a AbstractFramework object
      throws CCAException
      """
      return FrameworkHandle()

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
      svcs.initialize(self, cid, selfProperties, True) 
      self.d_instance[uniqueName].component = None
      self.d_instance[uniqueName].services = svcs
      self.d_aliases[uniqueName] = selfClassName
      return svcs

   def releaseServices(self, services):
      """
      input: a Services object
      output: a AbstractFramework object
      throws CCAException
      """
      if services != None:
         cid = services.getComponentID()
         instanceName = cid.getInstanceName()
         if instanceName in self.d_aliases.keys() :
            n_removed_instances = removeInstance(instanceName)
            n_removed_aliases = self.d_aliases.pop(instanceName, None)
            if n_removed_instances != 1 or n_remove_aliases == None :
               print "Unexpected behavior removind instances."
               print "n_removed_instances: " + n_removed_instances
               print "n_removed_aliases: " + n_removed_aliases
         else :
            print "Error: releaseServices() called on services object not created by getServices()"
      return

   def shutdownFramework(self):
      """
      input: none
      output: void
      throws CCAException
      """
      for instanceName in self.d_instance:
         removeInstance(instanceName)
  
   # Methods from BuilderService
   def createInstance(self, instanceName, className, properties):
      """
      Our components are Python classes. The className is in the format xxx.xxx.xxx.Class, where the xxx. 
      stands for the module to be imported and the Class is the name of the class. The xxx. part may be
      repeated. For example, in doe.cca.Library.GaussianElimination, doe.cca.Library is the module name
      and GaussianElimination is the class. 
      We could, in theory, use the properties TypeMap to pass parameters to the component object constructor.
      But I will not do it. Let the calling entity call a initialize method.
      input: a string instanceName, a string className, a gov.cca.TypeMap properties
      output: a gov.cca.ComponentID object
      throws CCAException
      """
      moduleName = className.split('.')[0:-1]
      moduleName = ".".join(moduleName)
      className_ = className.split('.')[-1]
      class_ =  getattr(importlib.import_module(moduleName), className_)
      component = class_() 

      uniqueName = getUniqueName(instanceName)
      cid = ComponentID(None)
      cid.initiliaze(uniqueName)
      services = ServicesHandle()
      services.initialize(self, cid, properties, False)
      self.d_instance[uniqueName].component = component
      self.d_instance[uniqueName].services = services
      component.setServices(services)

      return cid

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


