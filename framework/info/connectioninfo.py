import CCAPython.gov.cca
import CCAPython.gov.cca.ports

class ConnectionID(CCAPython.gov.cca.ConnectionID):
   def __init__(self):
      return
   
   # New Methods
   def initialize(self, provider, providerPortName, user, userPortName, properties):
      """
      input: a CCAPython.gov.cca.ComponentID object provider, a string providerPortName, a CCAPython.gov.cca.ComponentID object user, a string userPortName
      output: a CCAPython.gov.cca.ConnectionID object
      throws CCAException
      """
      self.provider = provider
      self.providerPortName = providerPortName
      self.user = user
      self.userPortName = userPortName
      self.properties = properties

   def setProperties(self, properties):
      """
      input: a CCAPython.gov.cca.TypeMap object properties
      output: none
      """
      self.properties = properties

   def getProperties(self):
      """
      input: none
      output: a CCAPython.gov.cca.TypeMap object
      """
      return properties

   def isSame(self, cid):
      """
      This method returns True if the objects stand for the same connection.
      input: a ConnectionID cid
      ouput: boll
      """
      if self.provider.getInstanceName() == cid.provider.getInstanceName() :
         if self.user.getInstanceName() == cid.user.getInstanceName() :
            if self.providerPortName == cid.providerPortName :
               if self.userPortName == cid.userPortName :
                  return True
      else :
         return False

   # Methods from CCAPython.gov.cca.ConnectionID
   def getProvider(self):
      return self.provider

   def getUser(self):
      return self.user

   def getProviderPortName(self):
      return self.providerPortName

   def getUserPortName(self):
      return self.userPortName

class ConnectionEvent(CCAPython.gov.cca.ports.ConnectionEvent):
   def __init__(self, eventType, portInfo):      
      self.eventType = eventType
      self.portInfo = portInfo

   def initialize(self, eventType, portProperties):
      self.eventType = eventType
      self.portInfo = portProperties

   def getEventType(self):
      return self.eventType

   def getPortInfo(self):
      return self.portInfo

