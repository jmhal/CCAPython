import gov.cca
import gov.cca.ports

class ConnectionID(gov.cca.ConnectionID):
   def __init__(self):
   
   # New Methods
   def initialize(self, provider, providerPortName, user, userPortName, properties):
      """
      input: a gov.cca.ComponentID object provider, a string providerPortName, a gov.cca.ComponentID object user, a string userPortName
      output: a gov.cca.ConnectionID object
      throws CCAException
      """
      self.provider = provider
      self.providerPortName = providerPortname
      self.user = user
      self.userPortname = userPortName
      self.properties = properties

   def setProperties(self, properties):
      """
      input: a gov.cca.TypeMap object properties
      output: none
      """
      self.properties = properties

   def getProperties(self):
      """
      input: none
      output: a gov.cca.TypeMap object
      """
      return properties

   # Methods from gov.cca.ConnectionID
   def getProvider(self):
      return self.provider

   def getUser(self):
      return self.user

   def getProviderPortName(self):
      return self.providerPortName

   def getUserPortName(self):
      return self.userPortName

class ConnectionEvent(gov.cca.ports.ConnectionEvent):
   def __init__(self, eventType, portInfo):      
      self.eventType = eventType
      seff.portInfo = portInfo

   def initialize(self, eventType, portProperties):
      self.eventType = eventType
      self.portInfo = portProperties

   def getEventType(self):
      return self.eventType

   def getPortInfo(self):
      return self.portInfo

