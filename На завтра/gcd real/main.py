import random
import time
import xlwt

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_random_numbers():
    return random.randint(4300, 9000), random.randint(4300, 9000)

def save_to_text_file(result):
    with open('gcd_results.txt', 'a') as file:
        file.write(result + '\n')

def save_to_excel(result):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('GCD Results')
    sheet.write(0, 0, 'GCD')
    sheet.write(0, 1, 'Time (seconds)')
    for i, item in enumerate(result):
        sheet.write(i + 1, 0, item[0])
        sheet.write(i + 1, 1, item[1])
    workbook.save('gcd_results.xls')

def main():
    results = []
    for _ in range(10):  # Выполним операцию 10 раз для примера
        a, b = generate_random_numbers()
        start_time = time.time()
        result = gcd(a, b)
        end_time = time.time()
        execution_time = end_time - start_time
        results.append((result, execution_time))
        save_to_text_file(f'GCD of {a} and {b} is {result}. Execution time: {execution_time} seconds.')
    save_to_excel(results)

if __name__ == "__main__":
    main()
