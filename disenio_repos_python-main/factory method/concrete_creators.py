from creator import Creator
from product import ConcreteProductA, ConcreteProductB

class ConcreteCreatorA(Creator):
    def factoryMethod(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factoryMethod(self):
        return ConcreteProductB()