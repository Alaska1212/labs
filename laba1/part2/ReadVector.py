from Vector import Vector
class ReadVector:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        vectors = []
        with open(self.file_name, "r") as f:
            for line in f:
                components = list(map(float, line.strip().split()))
                vector = Vector(components)
                vectors.append(vector)
            return vectors

reader =  ReadVector("input01.txt")
print(reader.readline())