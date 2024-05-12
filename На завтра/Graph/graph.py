import matplotlib.pyplot as plt


def plot_text(text):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Отображаем текст
    ax.text(5, 5, text, fontsize=24, ha='center', va='center')

    # Получаем позиции букв
    positions, labels = [], []
    for char in text:
        x, y = ax.transData.transform((5, 5))  # координаты центра текста
        x_offset, y_offset = ax.transData.transform((1, 1))  # смещение от центра
        positions.append((x, y))
        labels.append(char)

    # Отображаем каждую букву в виде точек
    for pos, label in zip(positions, labels):
        ax.text(pos[0], pos[1], label, fontsize=24, ha='center', va='center')

    # Соединяем точки прямыми линиями
    for i in range(len(positions) - 1):
        ax.plot([positions[i][0], positions[i + 1][0]], [positions[i][1], positions[i + 1][1]], 'k-')

    ax.axis('off')
    plt.show()


def main():
    text = input("Введите текст для отображения на графике: ")
    plot_text(text)


if __name__ == "__main__":
    main()


