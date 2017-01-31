import gov.cca
import gov.cca.ports

class HelloClientGoPort(gov.cca.ports.GoPort):
   def __init__(self, component):
      self.component = component
      super(HelloClientGoPort, self).__init__()
      return

   def go(self):
      port = self.component.services.getPort("HelloServer")
      port.sayHello()
      self.component.services.releasePort("HelloServer")
      return

class Component(gov.cca.Component):
   def __init__(self):
      self.goPort = HelloClientGoPort(self)
      return

   def setServices(self, services):
      self.services = services
      services.registerUsesPort("HelloServer", "examples.HelloWorld.HelloServer.StringProducerPort", None)
      services.addProvidesPort(self.goPort, "GoPort", "gov.cca.ports.GoPort", None)
      return

      

