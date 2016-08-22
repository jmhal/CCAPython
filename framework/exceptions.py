from gov.cca import CCAException
from gov.cca import CCAExceptionType

class TypeMismatchException(CCAException):
   def __init__(self, exceptionType):
      self.exceptionType = exceptionType
   
   def initialize(self, requestedType, actualType):
      self.requestedType = requestedType
      self.actualType = actualType

   def getCCAExceptionType(self):
      return self.exceptionType

   def getRequestedType(self):
      return self.requestedType

   def getActualType(self):
      return self.ActualType



