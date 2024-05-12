def chinese_remainder_theorem(num_list, rem_list):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def mod_inverse(a, m):
        gcd, x, y = extended_gcd(a, m)
        if gcd != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    n = 1
    for num in num_list:
        n *= num

    result = 0
    for i, num in enumerate(num_list):
        ni = n // num
        result += rem_list[i] * ni * mod_inverse(ni, num)

    return result % n

def main():
    num_list = list(map(int, input("Введите числа через пробел: ").split()))
    rem_list = list(map(int, input("Введите остатки через пробел: ").split()))
    try:
        result = chinese_remainder_theorem(num_list, rem_list)
        print("Solution for x:", result)
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()

