def g(x, k):
    x0 = 1
    yield x0
    for i in range(1, k+1):
        x0 *= -x*(i-1)/i
        yield x0


x = int(input('х = '))
x0 = -x
k = int(input('член послідовності: '))
for i in range(2, k+1):
    x0 *= -x*(i-1)/i

x0 = x
for i in g(x, k):
    x0 = i

print(x0)