from gov.cca import Services
from gov.cca.ports import ConnectionEventService

class ServiceHandle(Services, ConnectionEventService):
   def __init__(self):
      pass
 
   # New methods
   def initialize(self, fwk, componentID, properties):
      """
      input: a gov.cca.AbstractFramework fwk, a gov.cca.ComponentID componentID and a gov.cca.TypeMap properties
      ouput: void
      """
      pass
  
   def getInstanceProperties():
      """
      input: none
      output: a gov.cca.TypeMap object
      """
      pass
   
   def setInstanceProperties(self, properties):
      """
      input: a gov.cca.TypeMap properties
      output: none
      """
      pass

   def setPortProperties(self, portName, properties):
      """
      input: a string portName, a gov.cca.TypeMap properties
      output: none
      """
      pass

   def getProviderPortNames(self):
      """
      input: none
      output: a list of strings
      """
      pass

   def getUsedPortNames(self):
      """
      input: none
      output: a list of strings
      """
      pass


   def bindPort(self, portName, port):
      """
      input: a string portName, a gov.cca.Port object
      output: void
      """
      pass

   def getProvidesPort(self, name):
      """
      input: string name
      output: void
      """
      pass

   def notifyConnectionEvent(self, portName, event):
      """
      input: string portName, a gov.cca.ports.EventType event)
      output: void
      """
      pass

