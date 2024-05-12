def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x


def main():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    gcd, x, y = egcd(a, b)
    print(f"НОД({a}, {b}) = {gcd}")
    print(f"Коэффициенты x и y: {x}, {y}")


if __name__ == "__main__":
    main()
