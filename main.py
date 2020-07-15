import tkinter as tk
from PIL import ImageTk, Image

direction = 'up'
player_bbox = (240, 240, 260, 260)
UPDATE_TIME = 100
apple_coords = (0, 0)
apple_img = None

class Board(tk.Canvas):
    global direction

    def __init__(self, master):
        super().__init__(bg='black', master=master)
        self.initGame()
        self.pack(fill=tk.BOTH, expand=1, padx=2, pady=2)

    def initGame(self):
        self.create_entities()

        self.bind_all("<Key>", self.key_press)
        self.after(500, self.move_player)
        pass

    def create_entities(self):
        self.player = self.create_rectangle(player_bbox, tags='player', fill='white', outline='white')
        apple_img = ImageTk.PhotoImage(Image.open('res/apple.png'))
        self.image = apple_img
        self.apple = self.create_image(apple_coords, tags='apple', image=apple_img)
        self.score = self.create_text(480, 5, anchor='ne', text='Score: 0', fill='white')

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
            print('Height:', self.winfo_height())
            print('Width:', self.winfo_width())

    # Game loop
    def move_player(self):
        dx, dy = self.get_movement()

        self.move(self.player, dx, dy)

        self.after(UPDATE_TIME, self.move_player)

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
