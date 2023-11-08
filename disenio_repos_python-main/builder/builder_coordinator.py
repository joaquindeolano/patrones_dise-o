from concrete_builder import ConcreteBuilder

class Builder_coordinator:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build1()
        self.builder.build2()