VERSION = "0.1a"

class Port(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")  

class Component(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")
   
   def setServices(self, services):
      """
      input: services object.
      output: void 
      """
      raise NotImplementedError("Abstract Class!")

class ComponentRelease(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")
   
   def releaseServices(self, services):
      """
      input: services object.
      output: void 
      """
      raise NotImplementedError("Abstract Class!")

class ComponentID(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")
  
   def getInstanceName(self):
      """
      input: none
      output: a string identifier for the component (uuid?).
      throws CCAException.
      """
      raise NotImplementedError("Abstract Class!")
  
   def getSerialization(self):
      """
      input: none
      output: a serialization of the object sufficient for saving the component's state to disk and restart at a different time.
      throws CCAException.
      """
      raise NotImplementedError("Abstract Class!")

class Services(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def getComponentID(self):
      """
      input: none
      output: a ComponentID object
      """
      raise NotImplementedError("Abstract Class!")

   def createTypeMap(self):
      """
      input: none
      output: a TypeMap object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def registerUsesPort(self, portName, type, properties):
      """
      input: string portName, string type, and TypeMap properties
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")
  
   def unregisterUsesPort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")
 
   def addProvidesPort(self, inPort, portName, type, properties):
      """
      input: Port inPort, string portName, string type, and TypeMap properties
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")
  
   def removeProvidesPort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def getPortProperties(self, portName):  
      """
      input: string portName
      output: a TypeMap object 
      """
      raise NotImplementedError("Abstract Class!")

   def getPort(self, portName):
      """
      input: string portName
      output: a Port object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def getPortNonblocking(self, portName):
      """
      input: string portName
      output: a Port object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def releasePort(self, portName):
      """
      input: string portName
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def registerForRelease(self, callback):
      """
      input: a gov.cca.ComponentRelease object callback
      output: void
      """
      raise NotImplementedError("Abstract Class!")

class AbstractFramework(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def createTypeMap(self):
      """
      input: none 
      output: a TypeMap object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def createEmptyFramework(self):
      """
      input: none 
      output: a AbstractFramework object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def getServices(self, selfInstanceName, selfClassName, selfProperties):
      """
      input: a string selfInstanceName, string selfClassName, TypeMap selfProperties
      output: a Services object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def releaseServices(self, services):
      """
      input: a Services object
      output: a AbstractFramework object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def shutdownFramework(self):
      """
      input: none
      output: void
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

class ComponentClassDescription(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def getComponentClassName(self):
      """
      input: none 
      output: a string
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

class ConnectionID(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def getProvider(self):
      """
      input: none 
      output: a ComponentID object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def getUser(self):
      """
      input: none 
      output: a ComponentID object
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def getProviderPortName(self):
      """
      input: none 
      output: a string
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")

   def getUserPortName(self):
      """
      input: none 
      output: a string
      throws CCAException
      """
      raise NotImplementedError("Abstract Class!")


class Type(object):
   none, Int, Long, Float, Double, Fcomplex, Dcomplex, String, Bool, IntArray, LongArray, FloatArray, DoubleArray, FcomplexArray, DComplexArray, StringArray, BoolArray = range(17)
   
   def __init__(self):
      raise NotImplementedError("Enumeration!")

class TypeMap(object):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")

   def getInt(self, key, dflt):
      """
      input: string key, integer dflt
      output: a integer
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getLong(self, key, dflt):
      """
      input: string key, long dflt
      output: a long
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getFloat(self, key, dflt):
      """
      input: string key, float dflt
      output: a float
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getDouble(self, key, dflt):
      """
      input: string key, double dflt
      output: a double
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getFcomplex(self, key, dflt):
      """
      input: string key, fcomplex dflt
      output: a fcomplex
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getDcomplex(self, key, dflt):
      """
      input: string key, dcomplex dflt
      output: a dcomplex
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getString(self, key, dflt):
      """
      input: string key, string dflt
      output: a integer
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getBool(self, key, dflt):
      """
      input: string key, bool dflt
      output: a boolean
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def getIntArray(self, key, dflt):
      """
      input: string key, int dflt
      output: a list of int
      """
      raise NotImplementedError("Abstract Class!")

   def getLongArray(self, key, dflt):
      """
      input: string key, long dflt
      output: a list of long
      """
      raise NotImplementedError("Abstract Class!")

   def getFloatArray(self, key, dflt):
      """
      input: string key, float dflt
      output: a list of float
      """
      raise NotImplementedError("Abstract Class!")

   def getDoubleArray(self, key, dflt):
      """
      input: string key, double dflt
      output: a list of double
      """
      raise NotImplementedError("Abstract Class!")

   def getFcomplexArray(self, key, dflt):
      """
      input: string key, fcomplex dflt
      output: a list of fcomplex
      """
      raise NotImplementedError("Abstract Class!")

   def getDcomplexArray(self, key, dflt):
      """
      input: string key, dcomplex dflt
      output: a list of dcomplex
      """
      raise NotImplementedError("Abstract Class!")

   def getStringArray(self, key, dflt):
      """
      input: string key, string dflt
      output: a list of string
      """
      raise NotImplementedError("Abstract Class!")

   def getBoolArray(self, key, dflt):
      """
      input: string key, bool dflt
      output: a list of bool
      """
      raise NotImplementedError("Abstract Class!")

   def putInt(self, key, value):
      """
      input: string key, integer value
      output: void 
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putLong(self, key, value):
      """
      input: string key, long value
      output: void
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putFloat(self, key, value):
      """
      input: string key, float value
      output: void
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putDouble(self, key, value):
      """
      input: string key, double value
      output: void
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putFcomplex(self, key, value):
      """
      input: string key, fcomplex value
      output: void
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putDcomplex(self, key, value):
      """
      input: string key, dcomplex value
      output: void
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putString(self, key, value):
      """
      input: string key, string value
      output: void
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putBool(self, key, value):
      """
      input: string key, bool value
      output: void
      throws TypeMismatchException
      """
      raise NotImplementedError("Abstract Class!")

   def putIntArray(self, key, value):
      """
      input: string key, int list value
      output: void 
      """
      raise NotImplementedError("Abstract Class!")

   def putLongArray(self, key, value):
      """
      input: string key, long list value
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def putFloatArray(self, key, value):
      """
      input: string key, float list value
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def putDoubleArray(self, key, value):
      """
      input: string key, double list value
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def putFcomplexArray(self, key, value):
      """
      input: string key, fcomplex list value
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def putDcomplexArray(self, key, value):
      """
      input: string key, dcomplex list value
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def putStringArray(self, key,  value):
      """
      input: string key, string list value
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def putBoolArray(self, key, value):
      """
      input: string key, bool list value
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def cloneTypeMap(self):
      """
      input: none
      output: a TypeMap object
      """
      raise NotImplementedError("Abstract Class!")
  
   def cloneEmpty(self):
      """
      input: none
      output: a TypeMap object
      """
      raise NotImplementedError("Abstract Class!")

   def remove(self, key):
      """
      input: a string key
      output: void
      """
      raise NotImplementedError("Abstract Class!")

   def getAllKeys(self, t):
      """
      input: Type object t
      output: a list of strings
      """
      raise NotImplementedError("Abstract Class!")

   def hasKey(self, key):
      """
      input: a string key
      output: boolean
      """
      raise NotImplementedError("Abstract Class!")

   def typeOf(self, key):
      """
      input: a string key
      output: a Type object
      """
      raise NotImplementedError("Abstract Class!")


class CCAExceptionType(object):
   Unexpected = -1
   Nonstandard = 1
   PortNotDefined = 2
   PortAlreadyDefined = 3
   PortNotConnected = 4
   PortNotInUse = 5
   UsesPortNotReleased = 6
   BadPortName = 7
   BadPortType = 8
   BadProperties = 9
   BadPortInfo = 10
   OutOfMemory = 11
   NetworkError = 12
   def __init__(self):
      raise NotImplementedError("Enumeration!")

class CCAException(Exception):
   def __init__(self):
      raise NotImplementedError("Abstract Class!")
   
   def getCCAExceptionType(self):
      """
      input: none 
      output: a CCAException object
      """
      raise NotImplementedError("Abstract Class!")

   def setCCAExceptionType(self, exceptionType):
      """
      input: a field from CCAExceptionType 
      output: a CCAException object
      """
      raise NotImplementedError("Abstract Class!")


