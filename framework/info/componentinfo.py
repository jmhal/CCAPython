import CCAPython.gov.cca
import CCAPython.gov.cca.ports

class ComponentID(CCAPython.gov.cca.ComponentID):
   def __init__(self, name):
      self.name = name
  
   def initialize(self, name):
      self.name = name 
   
   def getInstanceName(self):
      return self.name

   def getSerialization(self):
      return self.name 

class ComponentClassDescription(CCAPython.gov.cca.ComponentClassDescription):
   def __init__(self, dscp):
      self.description = dscp

   def getComponentClassName(self):
      return self.description

class ComponentRepository(CCAPython.gov.cca.ports.ComponentRepository):
   def __init__(self):
      self.repository = {}

   def getAvailableComponentClasses(self):
      return self.repository
