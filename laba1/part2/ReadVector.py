from Vector import Vector


files = ("input01.txt.txt", "input02.txt.txt", "input03.txt.txt", "input04.txt")

for name in files:
    with open(name, 'r') as f:
        max_dim = (0, 0)
        max_module = (0, 0)

        sum = 0
        counter = 0

        max_coord = (0, 0)
        min_coord = (0, 0)

        vectors = []
        for line in f:

            if line == "\n":
                continue

            line = line.split()
            args = []
            for coord in line:
                args.append(int(coord))

            v = Vector(*args)
            sum += v.module()
            vectors.append(v)

            if v.dim() >= max_dim[0]:
                if v.dim() == max_dim[0]:
                    if v.module() < max_dim[1].module():
                        max_dim = (v.dim(), v)
                else:
                    max_dim = (v.dim(), v)

            if v.module() >= max_module[0]:
                if v.module() == max_module[0]:
                    if v.dim() < max_module[1].dim():
                        max_module = (v.module(), v)
                else:
                    max_module = (v.module(), v)

            if v.max() >= max_coord[0]:
                if max_coord[0] == v.max():
                    if v.min() < max_coord[1].min():
                        max_coord = (v.max(), v)
                else:
                    max_coord = (v.max(), v)

            if min_coord[0] >= v.min():
                if min_coord[0] == v.min():
                    if v.max() > min_coord[1].max():
                        min_coord = (v.min(), v)
                else:
                    min_coord = (v.min(), v)

        mean_mod = sum / len(vectors)

        for vector in vectors:
            if vector.module() > mean_mod:
                counter += 1

        print(f"{name}\n")
        print(f"найбільша розмірність - {max_dim[0]}, вектор - {max_dim[1].show()}\n")
        print(f"найбільша довижна - {max_module[0]}, вектор - {max_module[1].show()}\n")
        print(f"середня довжина вектора - {mean_mod}, кількість векторів з більшою за середню довжину - {counter}\n")
        print(f"найменшу компоненту - {min_coord[0]}, вектор - {min_coord[1].show()}\n")
        print(f"найбільшу компоненту - {max_coord[0]}, вектор - {max_coord[1].show()}\n")