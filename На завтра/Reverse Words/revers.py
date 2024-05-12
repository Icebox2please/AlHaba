def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def main():
    input_text = input("Введите текст для переворачивания слов: ")
    reversed_text = reverse_words(input_text)
    print("Результат:", reversed_text)

if __name__ == "__main__":
    main()