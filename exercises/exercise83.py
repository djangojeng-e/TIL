def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1) + 100

print(f(5))