from abstract_factory import AbstractFactory
from concrete_products import ProductoA_1, ProductoB_1, ProductoA_2, ProductoB_2

class ConcreteFactory_1(AbstractFactory):
    def CrearProducto_A(self):
        return ProductoA_1()

    def CrearProducto_B(self):
        return ProductoB_1()

class ConcreteFactory_2(AbstractFactory):
    def CrearProducto_A(self):
        return ProductoA_2()

    def CrearProducto_B(self):
        return ProductoB_2()