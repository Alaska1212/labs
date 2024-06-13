x = float(input('х =1 '))
x0 = x
s = x
eps = 10 ** -13
n = 1
while abs(x0) > eps:
    x0 *= - x**2 * (2 * n - 1) / (n * (2 * n + 1))
    n += 1
    s += x0

print(s)
print('n =', n)