# coding: utf-8

import time
import Tkinter as tkinter

SIZE = 200
LEFT = -2
RIGHT = 0.5
TOP = 1.25
BOTTOM = -1.25
ITERATIONS = 20

root = tkinter.Tk()
can = tkinter.Canvas(width=250, height=200)
can.pack()

UPDATE_TIME = 0.2
next_update = time.time() + UPDATE_TIME
for y in range(SIZE):
        for x in range(SIZE):
                z = complex(0, 0)
                c = complex(LEFT + x * (RIGHT - LEFT) / SIZE, TOP + y * (BOTTOM - TOP) / SIZE)
                norm = abs(z) ** 2
                for count in range(ITERATIONS):
                        if norm <= 4.0:
                                z = complex(z.real * z.real - z.imag * z.imag + c.real, z.imag * z.real * 2 + c.imag)
                                norm = abs(z) ** 2
                if norm <= 0.05:
                        can.create_text(x, y, fill='black', text='.')
                elif norm <= 0.10:
                        can.create_text(x, y, fill='green', text='.')
                elif norm <= 0.15:
                        can.create_text(x, y, fill='blue', text='.')
                elif norm <= 0.20:
                        can.create_text(x, y, fill='red', text='.')
                elif norm <= 0.25:
                        can.create_text(x, y, fill='yellow', text='.')
                elif norm <= 0.30:
                        can.create_text(x, y, fill='grey', text='.')

                if time.time() > next_update:
                    next_update = time.time() + UPDATE_TIME
                    root.update()

root.mainloop()