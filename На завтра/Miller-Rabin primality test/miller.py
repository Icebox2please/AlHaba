import random

def miller_rabin_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Выразим n - 1 как (2^r) * d, где d - нечетное
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Произведем k тестов Миллера-Рабина
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    num = int(input("Введите число для проверки простоты: "))
    k = int(input("Введите количество итераций (рекомендуется 5): "))
    if miller_rabin_test(num, k):
        print(f"{num} - простое число")
    else:
        print(f"{num} - составное число")

if __name__ == "__main__":
    main()
