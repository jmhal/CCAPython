#!/usr/bin/python
from framework.manage.builders import FrameworkHandle

fwk = FrameworkHandle()

matrix_A = fwk.createInstance("MatrixAInstance", "examples.MatrixMultiplication.Matrix.Component", None)

filePort = fwk.lookupPort(matrix_A, "FileSystemManagement")   
filePort.loadMatrixFromFile("/home/joaoalencar/repositorios/parallel/python/matrix/matrix_A.mtr")
#filePort.createZeroMatrix(5);

dataPort = fwk.lookupPort(matrix_A, "DataAccess")
print dataPort.getItem(0,0)
dataPort.setItem(0, 0, 1984)
print dataPort.getItem(0,0)
#dataPort.printMatrix()
   
      

