from Rational import Rational
from RationalList import RationalList


res = open('res.txt', 'w')
files = ['input01.txt', 'input02.txt', 'input03.txt']
for file in files:
    with open(file) as f:
        a = RationalList([])
        new = []
        for line in f:
            if line.split() != []:
                data = [el for el in line.split()]
                for num in data:
                    if '/' in num:
                        new = a + Rational(num)
                    else:
                        new = a + Rational(int(num))

        res.write(f'{sum(new)} \n')