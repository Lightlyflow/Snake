import tkinter as tk

direction = 'up'

class Board(tk.Canvas):
    def __init__(self, master):
        super().__init__(bg='black', master=master)
        self.initGame()
        self.pack(fill=tk.BOTH, expand=1, padx=2, pady=2)

    def initGame(self):
        self.bind_all("<Key>", self.key_press)
        self.after()
        pass

    def key_press(self, event):
        bpress = event.char
        if bpress == 'w':
            print('w')
        elif bpress == 'a':
            print('a')
        elif bpress == 's':
            print('s')
        elif bpress == 'd':
            print('d')


class Snake(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master, bg='blue')
        self.pack(fill=tk.BOTH, expand=1)
        board = Board(self)


root = tk.Tk()
root.geometry('500x500')
game = Snake(root)
root.mainloop()
