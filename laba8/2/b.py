from math import log, e

x = float(input('х = '))
x1 = x
s = x
eps = 10 ** -13
n = 1
while abs(x1) > eps:
    x1 *= -x * (n) / n
    n += 1
    s += x1

print(s)
print(log((1+x), e))