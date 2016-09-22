import gov.cca.Port
import gov.cca.Component

class StringProducerPort(gov.cca.Port):
   def __init__(self):
      pass

   def sayHello(self):
      print "Hello World"

class Component(gov.cca.Component):
   def __init__(self):
      self.stringProducerPort = StringProducerPort()
      return

   def setServices(self, services):
      self.services = services
      services.addProvidesPort(self.stringProducerPort, "HelloServer", "HelloServer.HelloPort", None):
      return 
      
