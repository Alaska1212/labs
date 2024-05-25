from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

names = ['input01.txt', 'input02.txt', 'input03.txt']
res = ['res01.txt', 'res02.txt', 'res03.txt']
k = 0

for file in names:
    res_file = open(res[k], 'w')
    one_solve = dict()
    with open(file) as f:
        for line in f:
            if line.split() != []:
                data = [int(el) for el in line.split()]
                if len(data) == 2:
                    a = Equation(*data)
                elif len(data) == 3:
                    a = QuadraticEquation(*data)
                else:
                    a = BiQuadraticEquation(data[0], data[2], data[4])

                if len(a.solve()) == 1:
                    one_solve[float(a.solve()[0])] = str(a)
                res_file.write(str(a) + '\n')
                res_file.write(str(a.solve()) + '\n')

    k += 1

    print(f"Рівняння з найменшим розв'язком {file}:", one_solve[min(one_solve)])
    print(f"Рівняння з найбільшим розв'язком {file}:", one_solve[max(one_solve)], '\n')