def euler_phi(n):
    result = n
    p = 3
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 2
    if n > 1:
        result -= result // n
    return result

def main():
    results = {}
    for num in range(1, 1001, 2):
        results[num] = euler_phi(num)
    for num, phi in results.items():
        print(f"Euler phi({num}) = {phi}")

if __name__ == "__main__":
    main()
