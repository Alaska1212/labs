def g(x, k):
    x0 = 1
    yield x0
    for i in range(1, k+1):
        x0 *= - x ** 2 / (2 * i * (2 * i - 1))
        yield x0


x = int(input('х = '))
x0 = 1
k = int(input('член послідовності: '))
for i in range(1, k+1):
    x0 *= - x ** 2 / (2 * i * (2 * i - 1))

x0 = 1
for i in g(x, k):
    x0 = i

print(x0)