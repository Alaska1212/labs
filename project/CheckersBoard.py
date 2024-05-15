import tkinter as tk

class CheckersBoard(tk.Frame):
    def __init__(self):
        super().__init__()
        self.pack()
        self.board = tk.Canvas(self, width=400, height=400)
        self.board.pack()
        self.draw_board()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = "black" if (i + j) % 2 == 0 else "white"
                self.board.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)

root = tk.Tk()
app = CheckersBoard()
app.mainloop()
