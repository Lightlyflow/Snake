import tkinter as tk
from random import random, randrange

from PIL import ImageTk, Image

direction = 'up'
player_bbox = (240, 240, 260, 260)
UPDATE_TIME = 100
apple_coords = (110, 110)
score = 0


class Board(tk.Canvas):
    global direction, score

    def __init__(self, master):
        super().__init__(bg='black', master=master)
        self.initGame()
        self.pack(fill=tk.BOTH, expand=1, padx=2, pady=2)

    def initGame(self):
        self.create_entities()

        self.bind_all("<Key>", self.key_press)
        self.after(500, self.game_loop)
        pass

    def create_entities(self):
        self.player = self.create_rectangle(player_bbox, tags='player', fill='white', outline='white')
        apple_img = ImageTk.PhotoImage(Image.open('res/apple.png'))
        self.image = apple_img
        self.apple = self.create_image(apple_coords, tags='apple', image=apple_img)
        self.score_text = self.create_text(480, 5, anchor='ne', text='Score: 0', fill='white')

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
        elif button_press == 'x':
            print('Apple loc:', self.coords(self.apple))

    def get_movement(self):
        temp_bbox = self.coords(self.player)

        dy = {'up': -20,
              'down': 20}.get(direction, 0)
        dx = {'right': 20,
              'left': -20}.get(direction, 0)

        # Apply theoretical changes
        temp_bbox[0] += dx
        temp_bbox[2] += dx
        temp_bbox[1] += dy
        temp_bbox[3] += dy

        x_bbox = temp_bbox[::2]
        y_bbox = temp_bbox[1::2]

        if min(x_bbox) < 0 or max(x_bbox) > 500:
            dx = 0
        if min(y_bbox) < 0 or max(y_bbox) > 500:
            dy = 0

        return dx, dy

    def isOverlapping(self) -> bool:
        global player_bbox

        player_bbox = self.coords(self.player)
        if len(self.find_overlapping(*player_bbox)) > 1:
            return True
        return False

    def move_apple(self):
        # TODO:: Check for snake body
        x, y = randrange(0, stop=500, step=20)+10, randrange(0, stop=500, step=20)+10

        self.coords(self.apple, x, y)

    # Game loop
    def game_loop(self):
        global score

        # Movement
        dx, dy = self.get_movement()
        self.move(self.player, dx, dy)

        # Collision with apple
        if self.isOverlapping():
            score += 1
            self.itemconfigure(self.score_text, text='Score: '+str(score))
            self.move_apple()

        self.after(UPDATE_TIME, self.game_loop)


class Snake(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master, bg='blue')
        self.pack(fill=tk.BOTH, expand=1)
        Board(self)


root = tk.Tk()
root.title('Snake')
root.geometry('504x504')
game = Snake(root)
root.mainloop()
