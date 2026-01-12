def factor_pairs(n):
    return [(i, n // i) for i in range(1, int(n**0.5) + 1) if n % i == 0]
print(factor_pairs(36))

