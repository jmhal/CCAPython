from __future__ import print_function
import gov.cca

class FileSystemManagementPort(gov.cca.Port):
   """
   This port should be used by the Driver to load the matrices.
   """
   def __init__(self, portType, _data):
      self.data = _data
      super(FileSystemManagementPort, self).__init__(portType)
      return

   def loadMatrixFromFile(self, filename):
      _file = open(filename, "r+")
      for line in _file.readlines():
         self.data.append([float(n) for n in line.rstrip().split(" ")])
      _file.close()
      return
 
   def saveMatrixToFile(self, filename):
      _file = open(filename, "w+")
      for line in self.data:
         _file.writelines([str(n) + " " for n in line])
         _file.write('\n')
      _file.close()   

   def createZeroMatrix(self, order):
      for i in range(order):
         self.data.append([0] * order)
      return 

class DataAccessPort(gov.cca.Port):
   """
   This port should be used by the multiplier component
   """
   def __init__(self, portType, _data):
      self.data = _data
      super(DataAccessPort, self).__init__(portType)
      return 
   
   def getOrder(self):
      return len(self.data)

   def getItem(self, i, j):
      return self.data[i][j]  
  
   def setItem(self, i, j, value):
      self.data[i][j] = value
      return 

   def printMatrix(self):
      for i in range(len(self.data)):
          for j in range(len(self.data)):
             print(str(self.data[i][j]), end=" ")
          print('')   
      return

class Component(gov.cca.Component):
   def __init__(self):
      self.data = []
      self.dataAccessPort = DataAccessPort("examples.MatrixMultiplication.Matrix.DataAccessPort", self.data)
      self.fileSystemManagementPort = FileSystemManagementPort("examples.MatrixMultiplication.Matrix.FileSystemManagementPort", self.data)
      return

   def setServices(self, services):
      self.services = services
      services.addProvidesPort(self.dataAccessPort, "DataAccess", "examples.MatrixMultiplication.Matrix.DataAccessPort", None)
      services.addProvidesPort(self.fileSystemManagementPort, "FileSystemManagement", "examples.MatrixMultiplication.Matrix.FileSystemManagementPort", None)
      return
