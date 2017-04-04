#!/usr/bin/python
from framework.manage.builders import FrameworkHandle

fwk = FrameworkHandle()

matrix_A = fwk.createInstance("MatrixAInstance", "examples.MatrixMultiplication.Matrix.Component", None)
matrix_B = fwk.createInstance("MatrixBInstance", "examples.MatrixMultiplication.Matrix.Component", None)
matrix_C = fwk.createInstance("MatrixCInstance", "examples.MatrixMultiplication.Matrix.Component", None)

filePortA = fwk.lookupPort(matrix_A, "FileSystemManagement")   
filePortA.loadMatrixFromFile("/home/joaoalencar/repositorios/parallel/python/matrix/matrix_A.mtr")

filePortB = fwk.lookupPort(matrix_B, "FileSystemManagement")   
filePortB.loadMatrixFromFile("/home/joaoalencar/repositorios/parallel/python/matrix/matrix_B.mtr")

filePortC = fwk.lookupPort(matrix_C, "FileSystemManagement")   
filePortC.loadMatrixFromFile("/home/joaoalencar/repositorios/parallel/python/matrix/matrix_B.mtr")

multiplicator = fwk.createInstance("MultiplicatorInstance", "examples.MatrixMultiplication.Multiplicator.Component", None)

fwk.connect(multiplicator, "MatrixADataAccess", matrix_A, "DataAccess") 
fwk.connect(multiplicator, "MatrixBDataAccess", matrix_B, "DataAccess")
fwk.connect(multiplicator, "MatrixCDataAccess", matrix_C, "DataAccess")

goport = fwk.lookupPort(multiplicator, "GoPort")
goport.go()

filePortC.saveMatrixToFile("/home/joaoalencar/repositorios/parallel/python/matrix/matrix_C.mtr")

fwk.destroyInstance(matrix_A, 0.0)
fwk.destroyInstance(matrix_B, 0.0)
fwk.destroyInstance(matrix_C, 0.0)
fwk.destroyInstance(multiplicator, 0.0)

