n = int(input())

x1 = '1'
x0 = '0'
a = '1'
for i in range(1, n+1):
    x = a + x1 + i * x0
    a = x


print(x)