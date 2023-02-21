import tkinter as tk
import random

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake_speed = 100
        self.food_spawn_speed = 500
        self.snake_block = 10
        self.food_block = 10
        self.snake_list = []
        self.snake_color = '#00FF00'
        self.food_x = 0
        self.food_y = 0
        self.growing = False

        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.create_snake()
        self.create_food()
        self.bind_keys()
        self.root.after(self.snake_speed, self.move_snake)
        self.root.after(self.food_spawn_speed, self.create_food)
        self.root.mainloop()

    def create_snake(self):
        for x in range(3):
            self.snake_list.append(self.canvas.create_rectangle(0 + (x * self.snake_block), 0, 10 + (x * self.snake_block), 10, fill=self.snake_color))

    def create_food(self):
        self.food_x = round(random.randrange(0, self.width - self.snake_block) / 10.0) * 10.0
        self.food_y = round(random.randrange(0, self.height - self.snake_block) / 10.0) * 10.0
        self.food = self.canvas.create_rectangle(self.food_x, self.food_y, self.food_x + self.food_block, self.food_y + self.food_block, fill="red")

    def bind_keys(self):
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

    def move_up(self, event=None):
        self.snake_speed = 100
        self.update_speed(-10, 0)

    def move_down(self, event=None):
        self.snake_speed = 100
        self.update_speed(10, 0)

    def move_left(self, event=None):
        self.snake_speed = 100
        self.update_speed(0, -10)

    def move_right(self, event=None):
        self.snake_speed = 100
        self.update_speed(0, 10)

    def update_speed(self, x, y):
        self.snake_speed = 100
        self.x = x
        self.y = y

    def move_snake(self):
        head = self.canvas.coords(self.snake_list[-1])
        x1, y1, x2, y2 = head
        x, y = (x1+x2)/2, (y1+y2)/2
        new_head = self.canvas.create_rectangle(x+self.snake_speed, y+self.snake_speed,
            x+self.snake_speed+self.snake_block,
            y+self.snake_speed+self.snake_block,
            fill=self.snake_color)
        self.snake_list.append(new_head)

        if self.growing:
            self.growing = False
        else:
            tail = self.snake_list.pop(0)
            self.canvas.delete(tail)

    def check_collision(self):
        head = self.canvas.coords(self.snake_parts[-1])
        x1, y1, x2, y2 = head
        x, y = (x1+x2)/2, (y1+y2)/2
        
        if x <= 0 or x >= self.canvas_width or y <= 0 or y >= self.canvas_height:
            self.game_over()
        
        for part in self.snake_parts[:-1]:
            if self.canvas.coords(part) == head:
                self.game_over()

    def game_over(self):
        self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, text="Game Over",
                                font=("Arial", 25), fill="red")
        self.running = False

if __name__ == "__main__":
    #root = tk.Tk()
    game = SnakeGame(200,200)
    #game.run()

