def contador(n):
    if n == 0:
        return [0, ]

    return [n, ] + contador(n - 1)


print(contador(6))