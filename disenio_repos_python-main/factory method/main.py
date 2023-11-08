from creator import Creator
from concrete_creators import ConcreteCreatorA, ConcreteCreatorB

def CodigoCliente(creador):
    print(creador.operation())

if __name__ == "__main__":
    creador_a = ConcreteCreatorA()
    creador_b = ConcreteCreatorB()

    CodigoCliente(creador_a)
    CodigoCliente(creador_b)