import tkinter as tk

direction = 'up'
player_bbox = (240, 240, 260, 260)


class Board(tk.Canvas):
    global direction

    def __init__(self, master):
        super().__init__(bg='black', master=master)
        self.initGame()
        self.pack(fill=tk.BOTH, expand=1, padx=2, pady=2)

    def initGame(self):
        self.create_player()

        self.bind_all("<Key>", self.key_press)
        self.after(500, self.move_player)
        pass

    def create_player(self):
        self.player = self.create_rectangle(player_bbox, tags='player', fill='white', outline='white')

    def key_press(self, event):
        global direction
        button_press = event.char
        if button_press == 'w':
            direction = 'up'
        elif button_press == 'a':
            direction = 'left'
        elif button_press == 's':
            direction = 'down'
        elif button_press == 'd':
            direction = 'right'

    # Game loop
    def move_player(self):
        global player_bbox

        player_bbox = self.coords(self.player)
        dx, dy = 0, 0

        dy = {'up': -20,
              'down': 20}.get(direction, 0)
        dx = {'right': 20,
              'left': -20}.get(direction, 0)

        # if player_bbox ==

        self.move(self.player, dx, dy)

        self.after(100, self.move_player)


class Snake(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master, bg='blue')
        self.pack(fill=tk.BOTH, expand=1)
        Board(self)


root = tk.Tk()
root.geometry('500x500')
game = Snake(root)
root.mainloop()
