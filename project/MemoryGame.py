import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root, level=1):
        self.root = root
        self.root.title("Гра на тренування пам'яті")
        self.level = level
        self.color_matrix = self.get_color_matrix()

        # списки для кнопок та перевернутих карток
        self.buttons = []
        self.flipped = []

        self.create_board()

        # повідомлення про перемогу
        self.message_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.message_label.grid(row=self.rows, columnspan=self.cols)

    def get_color_matrix(self):
        if self.level == 1:
            colors = ['red', 'lime green', 'blue', 'yellow', 'orange red', 'purple'] * 2
            random.shuffle(colors)
            return [colors[i * 3:(i + 1) * 3] for i in range(4)]
        elif self.level == 2:
            colors = ['red', 'lime green', 'blue', 'yellow', 'orange red', 'purple', 'pink', 'LightSlateBlue'] * 2
            random.shuffle(colors)
            return [colors[i * 4:(i + 1) * 4] for i in range(4)]
        elif self.level == 3:
            colors = ['red', 'lime green', 'blue', 'yellow', 'orange red', 'purple', 'pink', 'LightSlateBlue', 'magenta', 'salmon'] * 2
            random.shuffle(colors)
            return [colors[i * 5:(i + 1) * 5] for i in range(4)]

    def create_board(self):
        # Створення ігрового поля з кнопками
        self.rows = len(self.color_matrix)
        self.cols = len(self.color_matrix[0])
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                button = tk.Button(self.root, bg='grey', width=20, height=10, command=lambda i=i, j=j: self.flip_card(i, j))
                button.grid(row=i, column=j)  # Розташовуємо кнопку в сітці
                row.append(button)
            self.buttons.append(row)  # Додаємо рядок кнопок до списку

    def flip_card(self, i, j):
        # Перевіряємо, чи кількість перевернутих карток менше 2 і чи картка ще не відкрита
        if len(self.flipped) < 2 and self.buttons[i][j]['bg'] == 'grey':
            # Змінюємо колір кнопки на відповідний колір з матриці
            self.buttons[i][j].config(bg=self.color_matrix[i][j])
            # Додаємо координати перевернутої картки до списку
            self.flipped.append((i, j))
            # Якщо перевернуті дві картки, перевіряємо збіг
            if len(self.flipped) == 2:
                self.root.after(1000, self.check_match)  # Затримка на 1 секунду перед перевіркою

    def check_match(self):
        # Отримуємо координати двох перевернутих карток
        i1, j1 = self.flipped[0]
        i2, j2 = self.flipped[1]
        # Якщо кольори карток збігаються
        if self.color_matrix[i1][j1] == self.color_matrix[i2][j2]:
            # Вимикаємо ці кнопки
            self.buttons[i1][j1].config(state='disabled')
            self.buttons[i2][j2].config(state='disabled')
        else:
            # Якщо кольори не збігаються, повертаємо кнопки до сірого кольору
            self.buttons[i1][j1].config(bg='grey')
            self.buttons[i2][j2].config(bg='grey')
        # Очищуємо список перевернутих карток
        self.flipped.clear()
        # Якщо всі кнопки вимкнені, виводимо повідомлення про перемогу
        if all(button['state'] == 'disabled' for row in self.buttons for button in row):
            self.message_label.config(text="Вітаємо! Ви відкрили всі кольори!")
            self.level += 1
            if self.level > 3:
                self.level = 1
            self.root.after(2000, self.restart_game)

    def restart_game(self):
        # Перезапускаємо гру з новим рівнем складності
        for row in self.buttons:
            for button in row:
                button.destroy()
        self.buttons.clear()
        self.flipped.clear()
        self.color_matrix = self.get_color_matrix()
        self.create_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
