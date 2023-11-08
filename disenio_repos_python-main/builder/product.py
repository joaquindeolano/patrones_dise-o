class Product:
    def __init__(self):
        self.part1 = None
        self.part2 = None

    def __str__(self):
        return f'Primera parte: {self.part1} / Segunda parte: {self.part2}'