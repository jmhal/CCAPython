import gov.cca
import gov.cca.ports

class MultiplicatorGoPort(gov.cca.ports.GoPort):

   def __init__(self, component):
      self.component = component
      super(MultiplicatorGoPort, self).__init__()
      return

   def go(self):
      portDataAccessMatrixA = self.component.services.getPort("MatrixADataAccess")
      portDataAccessMatrixB = self.component.services.getPort("MatrixBDataAccess")
      portDataAccessMatrixC = self.component.services.getPort("MatrixCDataAccess")

      matrix_order = portDataAccessMatrixA.getOrder()
      for i in range(matrix_order):
         for j in range(matrix_order):
            value = 0.0
            for k in range(matrix_order):
               a_value = portDataAccessMatrixA.getItem(i,k)
               b_value = portDataAccessMatrixB.getItem(k,j)
               value += a_value * b_value
            portDataAccessMatrixC.setItem(i, j, value)

      self.component.services.releasePort("MatrixADataAccess")
      self.component.services.releasePort("MatrixBDataAccess")
      return

class Component(gov.cca.Component):
   def __init__(self):
      self.goPort = MultiplicatorGoPort(self)
      return
 
   def setServices(self, services):
      self.services = services
      services.registerUsesPort("MatrixADataAccess", "examples.MatrixMultiplication.Matrix.DataAccessPort", None)
      services.registerUsesPort("MatrixBDataAccess", "examples.MatrixMultiplication.Matrix.DataAccessPort", None)
      services.registerUsesPort("MatrixCDataAccess", "examples.MatrixMultiplication.Matrix.DataAccessPort", None)
      services.addProvidesPort(self.goPort, "GoPort", "gov.cca.ports.GoPort", None)
      return

