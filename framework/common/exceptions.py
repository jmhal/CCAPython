from CCAPython.gov.cca import CCAException
from CCAPython.gov.cca import CCAExceptionType

class TypeMismatchException(CCAException):
   def __init__(self, exceptionType):
      self.exceptionType = exceptionType
   
   def initialize(self, requestedType, actualType):
      self.requestedType = requestedType
      self.actualType = actualType

   def getCCAExceptionType(self):
      return self.exceptionType
   
   def setCCAExceptionType(self, exceptionType):
      self.exceptionType = exceptionType
      return

   def getRequestedType(self):
      return self.requestedType

   def getActualType(self):
      return self.ActualType

class PortNotFoundException(CCAException):
   def __init__(self, portName):
      self.portName = portName
      self.exceptionType = CCAExceptionType.BadPortName

   def getCCAExceptionType(self):
      return self.exceptionType
   
   def setCCAExceptionType(self, exceptionType):
      self.exceptionType = exceptionType
      return

   def __str__(self):
      return "Port not found: " + self.portName

class InstanceNotFoundException(CCAException):
   def __init__(self, instanceName):
      self.instanceName = instanceName

   def getCCAExceptionType(self):
      return self.exceptionType
   
   def setCCAExceptionType(self, exceptionType):
      self.exceptionType = exceptionType
      return
   
   def __str__(self):
      return "Instance not found: " + self.instanceName

