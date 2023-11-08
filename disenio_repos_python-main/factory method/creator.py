from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factoryMethod(self):
        pass

    def operation(self):
        product = self.factoryMethod()
        return f"Operación en {product.operation()}"
