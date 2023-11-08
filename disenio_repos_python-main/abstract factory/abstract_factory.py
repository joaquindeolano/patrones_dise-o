from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def CrearProducto_A(self):
        pass

    @abstractmethod
    def CrearProducto_A_B(self):
        pass
    
    