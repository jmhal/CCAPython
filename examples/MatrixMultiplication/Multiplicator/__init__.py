import gov.cca
import gov.cca.ports

class MultiplicatorGoPort(gov.cca.ports.GoPort):

   def __init__(self, component):
      self.component = component
      super(MultiplicatorGoPort, self).__init__()
      return

   def go(self):
      



class Component(gov.cca.Component):
   def __init__(self):
      self.goPort = MultiplicatorGoPort(self)
      return
 
   def setServices(self, services):
      pass
