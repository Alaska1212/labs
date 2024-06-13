x = float(input('х = '))
x0 = 1
s = 1
eps = 10 ** -13
n = 1
while abs(x0) > eps:
    x0 *= x ** 2 / (2 * n)
    n += 1
    s += x0

print(s)
print('n =', n)