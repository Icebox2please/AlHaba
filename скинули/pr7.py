def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def china_town(residues, modulos):
    prod = 1
    for m in modulos:
        prod *= m
    result = 0

    for i in range(len(residues)):
        p = prod // modulos[i]
        _, inv, _ = gcd(p, modulos[i])
        result += residues[i] * inv * p

    return result % prod

residues = [20, 30, 30, 30, 5, 10, 60, 10, 30, 10, 10, 10, 10, 10]
modulos = [110, 100, 60, 50, 25, 20, 130, 120, 110, 100, 60, 50, 25, 20]

result = china_town(residues, modulos)
print("Решение системы уравнений: x =", result)
