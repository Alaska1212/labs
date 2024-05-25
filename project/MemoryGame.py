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

        self.board()

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

    def board(self):
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
        if len(self.flipped) < 2 and self.buttons[i][j]['bg'] == 'grey':
            self.buttons[i][j].config(bg=self.color_matrix[i][j])
            self.flipped.append((i, j))
            if len(self.flipped) == 2:
                self.root.after(1000, self.check)  # Затримка на 1 секунду перед перевіркою

    def check(self):
        i1, j1 = self.flipped[0]
        i2, j2 = self.flipped[1]
        if self.color_matrix[i1][j1] == self.color_matrix[i2][j2]:
            self.buttons[i1][j1].config(state='disabled') # робимо кнопку неактивною
            self.buttons[i2][j2].config(state='disabled')
        else:
            self.buttons[i1][j1].config(bg='grey')
            self.buttons[i2][j2].config(bg='grey')
        self.flipped.clear()
        if all(button['state'] == 'disabled' for row in self.buttons for button in row):
            self.message_label.config(text="Вітаємо! Ви відкрили всі кольори!")
            self.level += 1
            if self.level > 3:
                self.level = 1
            self.root.after(2000, self.restart_game)

    def restart_game(self):
        for row in self.buttons:
            for button in row:
                button.destroy()
        self.buttons.clear()
        self.flipped.clear()
        self.color_matrix = self.get_color_matrix()
        self.board()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
