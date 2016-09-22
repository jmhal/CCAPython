import gov.cca.Component
import gov.cca.ports.GoPort

class HelloClientGoPort(gov.cca.ports.GoPort):
   def __init__(self, component):
      self.component = component
      return

   def go(self):
      port = component.services.getPort("HelloServer")
      # replace for the method in the server port
      port.sayHello()
      component.services.releasePort("HelloServer")
      return

class Component(gov.cca.Component):
   def __init__(self):
      self.goPort = HelloClientGoPort(self)
      return

   def setServices(self, services):
      self.services = services
      services.registerUsesPort("HelloServer", "HelloServer.HelloPort", None)
      services.addProvidesPort(self.goPort, "GoPort", "gov.cca.ports.GoPort", None)
      return

      

