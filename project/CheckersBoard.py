import tkinter as tk

class CheckersBoard(tk.Frame):
    def __init__(self, color1="peru", color2="grey6"):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.pack()
        self.board = tk.Canvas(self, width=400, height=400)
        self.board.pack()
        self.draw_board()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = self.color1 if (i + j) % 2 == 0 else self.color2
                self.board.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)

root = tk.Tk()
app = CheckersBoard(color1="peru", color2="grey6")
app.mainloop()
