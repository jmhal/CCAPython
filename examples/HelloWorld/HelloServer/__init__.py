import gov.cca

class StringProducerPort(gov.cca.Port):
   def sayHello(self):
      print "Hello World"

class Component(gov.cca.Component):
   def __init__(self):
      self.stringProducerPort = StringProducerPort("examples.HelloWorld.HelloServer.StringProducerPort")
      return

   def setServices(self, services):
      self.services = services
      services.addProvidesPort(self.stringProducerPort, "HelloServer", "examples.HelloWorld.HelloServer.StringProducerPort", None)
      return 
      
