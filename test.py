n = int(input('n: '))
print((sum([1 / ((2*k + 1) ** 3) for k in range(_)])) for _ in range(n + 1))