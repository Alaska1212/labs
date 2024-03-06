class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return str(self.coordinates)

    def dimension(self): #розмірність
        return len(self.coordinates)

    def length(self): #довжина
        return sum(x**2 for x in self.coordinates)**0.5

    def average(self):
        return sum(self.coordinates) / len(self.coordinates)

    def max_component(self):
        return max(self.coordinates)

    def min_component(self):
        return min(self.coordinates)

