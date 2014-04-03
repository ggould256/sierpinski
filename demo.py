#!/usr/bin/env python3

import tkinter
import math
import random

CORNERS = [(10, 490), (490, 490), (250, (490 - (240 * math.sqrt(3.0))))]


class SierpinskiDemo(object):
    """
    A quick graphical demo of stochastic generation of the Sierpinski
    triangle.

    The algorithm is:
     * Lay out three corners of a triangle.
     * Pick one of those corners as a starting "cursor" location
     * Repeat forever:
       * Choose a random corner
       * Move the cursor half way from its current location to that corner
       * Draw a point at the cursor's new location

    A correctness proof of this method is quite elegant, but will not fit
    in this docstring; it is left as an exercise to the reader.
    """

    def __init__(self):
        """Create the TK window and initialize constants."""
        self.root = tkinter.Tk()
        self.window = tkinter.Canvas(self.root,
                                     width=500, height=500, bg="black")
        self.window.pack()
        self.cursor = CORNERS[0]
        self.delay = 1000

    def draw_frame(self):
        """Draw an outline of the triangle"""
        self.window.create_line(CORNERS[0][0], CORNERS[0][1],
                                CORNERS[1][0], CORNERS[1][1],
                                fill="dark gray")
        self.window.create_line(CORNERS[1][0], CORNERS[1][1],
                                CORNERS[2][0], CORNERS[2][1],
                                fill="dark gray")
        self.window.create_line(CORNERS[2][0], CORNERS[2][1],
                                CORNERS[0][0], CORNERS[0][1],
                                fill="dark gray")

    @classmethod
    def new_cursor_pos(cls, old):
        """Perform the cursor movement computation from old location
        @p old; @returns the new location."""
        target = random.choice(CORNERS)
        new_pos = ((old[0] + target[0]) / 2,
                   (old[1] + target[1]) / 2)
        return new_pos

    def draw_cursor(self, color):
        """Draws a point at the cursor location.  TK doesn't provide a
        mechanism to draw a point, so actually draws a degenerate
        line."""
        self.window.create_line(self.cursor[0], self.cursor[1],
                                self.cursor[0] + 1, self.cursor[1] + 1,
                                width=1, fill=color)

    def start(self):
        """Starts the drawing process."""
        self.window.after(0, self._tick)

    def _tick(self):
        """Draws a point, moves the cursor, and reschedules itself.
        The delay is reduced to create a gradual acceleration effect.
        """
        self.draw_cursor("white")
        self.cursor = self.new_cursor_pos(self.cursor)
        self.draw_cursor("red")
        self.delay *= 0.98
        self.window.after(int(self.delay) + 1, self._tick)


if __name__ == '__main__':
    demo = SierpinskiDemo()
    demo.draw_frame()
    demo.start()
    tkinter.mainloop()
