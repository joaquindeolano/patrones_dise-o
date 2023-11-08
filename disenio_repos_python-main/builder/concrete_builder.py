from product import Product
from builder import Builder

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build1(self):
        self.product.part1 = "Se ha construido correctamente la primera parte."

    def build2(self):
        self.product.part2 = "Se ha construido correctamente la segunda parte"

    def getProduct(self):
        return self.product