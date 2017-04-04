from CCAPython.gov.cca import TypeMap
from CCAPython.gov.cca import Type

class TypeMapDict(TypeMap):
   def __init__(self):
      self.map = {}

   def cloneTypeMap(self):
      newmap = {}
      for key in self.map.keys():
         newmap[key] = self.map[key]
      return newmap

   def cloneEmpty(self):
      newmap = {}
      for key in self.map.keys():
         newmap[key] = '' 
      return newmap

   def remove(self, key):
      if key in self.map.keys():
          self.map.pop(key)

   def getAllKeys(self, t):
      return self.map.keys()

   def hasKey(self, key):
      if key in self.map.keys():
         return True
      return False

   def typeOf(self, key):
      if isinstance(self.map[key], list):
         value = self.map[key]
         if len(valeu) == 0 :
            return Type.none
         else :
            firstValue = value[0]
            if isinstance(firstValue, int):
               return Type.IntArray 
            if isinstance(firstValue, long):
               return Type.LongArray 
            if isinstance(firstValue, float):
               return Type.FloatArray   
            if isinstance(firstValue, complex):
               return Type.FcomplexArray 
            if isinstance(firstValue, str):
               return Type.StringArray 
            if isinstance(firstValue, bool):
               return Type.BoolArray  
      else:
         if isinstance(self.map[key], int):
            return Type.Int 
         if isinstance(self.map[key], long):
            return Type.Long
         if isinstance(self.map[key], float):
            return Type.Float  
         if isinstance(self.map[key], complex):
            return Type.Fcomplex
         if isinstance(self.map[key], str):
            return Type.String
         if isinstance(self.map[key], bool):
            return Type.Bool 

   def put(self, key, value):
      self.map[key] = value

   def get(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         return self.map[key]

   def getInt(self, key, dflt):
      return int(self.get(key, dflt))

   def putInt(self, key, value):
      self.put(key, int(value))

   def getLong(self, key, dflt):
      return long(self.get(key, dflt))

   def putLong(self, key, value):
      self.put(key, long(value))

   def getFloat(self, key, dflt):
      return float(self.get(key, dflt))

   def putFloat(self, key, value):
      self.put(key, float(value))

   def getDouble(self, key, dflt):
      return float(self.get(key, dflt))

   def putDouble(self, key, value):
      self.put(key, float(value))

   def getFcomplex(self, key, dflt):
      return complex(self.get(key, dflt))

   def putFcomplex(self, key, value):
      self.put(key, complex(value))

   def getDcomplex(self, key, dflt):
      return complex(self.get(key, dflt))

   def putDcomplex(self, key, value):
      self.put(key, complex(value))

   def getString(self, key, dflt):
      return str(self.get(key, dflt))

   def putString(self, key, value):
      self.put(key, str(value))

   def getBool(self, key, dflt):
      return bool(self.get(key, dflt))

   def putBool(self, key, value):
      self.put(key, bool(value))

   def putIntArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(int(item))
      self.map[key] = newvalue

   def getIntArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(int(item))
         return newvalue
  
   def putLongArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(long(item))
      self.map[key] = newvalue

   def getLongArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(long(item))
         return newvalue
 
   def putFloatArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(float(item))
      self.map[key] = newvalue

   def getFloatArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(float(item))
         return newvalue

   def putDoubleArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(float(item))
      self.map[key] = newvalue

   def getDoubleArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(float(item))
         return newvalue
 
   def putFcomplexArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(complex(item))
      self.map[key] = newvalue

   def getFcomplexArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(complex(item))
         return newvalue
  
   def putDcomplexArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(complex(item))
      self.map[key] = newvalue

   def getDcomplexArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(complex(item))
         return newvalue
 
   def putStringArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(str(item))
      self.map[key] = newvalue

   def getStringArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(str(item))
         return newvalue

   def putBoolArray(self, key, value):
      newvalue = []
      for item in value:
         newvalue.append(bool(item))
      self.map[key] = newvalue

   def getBoolArray(self, key, dflt):
      if key not in self.map.keys():
         return dflt
      else: 
         newvalue = []
         for item in self.map[key]:
            newvalue.append(bool(item))
         return newvalue
 
 
 

if __name__ == "__main__":
   t = TypeMapDict()
   t.put("Coordenada", 1)
   coord = t.get("oordenada", 0)
   print coord
   t.putInt("Coordenada", 15)
   coord = t.getInt("Coordenada", 0)
   print coord
   t.putBool("verdade", True)
   st = t.getInt("verdade", 0)
   print st

   t.putIntArray("array", [1,2,"3"])
   ar = t.getIntArray("array", [])
   print ar
