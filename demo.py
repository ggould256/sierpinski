#!/usr/bin/env python3

import tkinter
import math
import random

CORNERS = [(10,490), (490, 490), (250, (490 - (240 * math.sqrt(3.0))))]

class SierpinskiDemo(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.window = tkinter.Canvas(self.root,
                                     width=500, height=500, bg="black")
        self.window.pack()
        self.cursor = CORNERS[0]
        self.delay = 1000

    def draw_frame(self):
        self.window.create_line(CORNERS[0][0], CORNERS[0][1],
                                CORNERS[1][0], CORNERS[1][1],
                                fill="gray")
        self.window.create_line(CORNERS[1][0], CORNERS[1][1],
                                CORNERS[2][0], CORNERS[2][1],
                                fill="gray")
        self.window.create_line(CORNERS[2][0], CORNERS[2][1],
                                CORNERS[0][0], CORNERS[0][1],
                                fill="gray")

    def new_cursor_pos(self, old):
        target = random.choice(CORNERS)
        new_pos = ((old[0] + target[0]) / 2,
                   (old[1] + target[1]) / 2)
        return new_pos

    def draw_cursor(self, color):
        self.window.create_line(self.cursor[0], self.cursor[1],
                                self.cursor[0] + 1, self.cursor[1] + 1,
                                width=1, fill=color)

    def start(self):
        self.window.after(0, self.tick)


    def tick(self):
        self.draw_cursor("white")
        self.cursor = self.new_cursor_pos(self.cursor)
        self.draw_cursor("red")
        self.delay *= 0.98
        self.window.after(int(self.delay) + 1, self.tick)


if __name__ == '__main__':
    demo = SierpinskiDemo()
    demo.draw_frame()
    demo.start()
    tkinter.mainloop()
