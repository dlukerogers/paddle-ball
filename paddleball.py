from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, score, color, start_x, start_y):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        randpos_x = random.randrange(start_x)
        randpos_y = random.randrange(start_y)
        self.canvas.move(self.id, randpos_x, randpos_y)
        self.x = 0
        self.y = 0
        self.canvas.bind_all('<Button-1>', self.start_game)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def start_game(self, evt):
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(starts)
        self.y = -3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            time.sleep(.5)
            canvas.create_text(250, 50, text='Game Over', fill='black', font='Helvetica 50 bold')
            canvas.pack()
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def change_color(self):
        colors = ['red','green','blue','yellow','orange','white','purple', 'black', 'grey', 'brown', 'pink', 'cyan']
        randcolor_onchange = random.choice(colors)
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.canvas.itemconfig(self.id, fill=randcolor_onchange)
        if pos[1] <= 0:
            self.canvas.itemconfig(self.id, fill=randcolor_onchange)
        if pos[2] >= self.canvas_width:
            self.canvas.itemconfig(self.id, fill=randcolor_onchange)

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

class Score:
    def __init__(self, canvas):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 25, text=f'Score = {self.score}', fill='black', font='Helvetica 17')

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=f'Score = {self.score}')
        
        

tk = Tk()
tk.title('Bounce Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
colors = ['red','green','blue','yellow','orange','white','purple']
randcolor_canvas = random.choice(colors)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, bg=randcolor_canvas)
canvas.pack()
tk.update();

randcolor_ball = random.choice(colors)
randcolor_paddle = random.choice(colors)
score = Score(canvas)
paddle = Paddle(canvas, randcolor_paddle)
ball = Ball(canvas, paddle, score, randcolor_ball, 500, 250)

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        ball.change_color()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
