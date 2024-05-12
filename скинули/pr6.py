import math

def euler(n):
    result = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            result += 1
    print(f'Функция Эйлера от {n} равна {result}')

for x in range(1001):
    if x % 2 != 0:
        euler(x)
    else:
        None