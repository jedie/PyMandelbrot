# coding: utf-8

import time
import Tkinter as tkinter

WIDTH = 320
HEIGHT = 240
LEFT = -2
RIGHT = 0.5
TOP = 1.25
BOTTOM = -1.25
ITERATIONS = 20

root = tkinter.Tk()
image = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
lb1 = tkinter.Label(root, image=image)
lb1.pack()

UPDATE_TIME = 0.2
start_time = time.time()
next_update = start_time + UPDATE_TIME
for y in range(HEIGHT):
    for x in range(WIDTH):
        z = complex(0, 0)
        c = complex(LEFT + x * (RIGHT - LEFT) / WIDTH, TOP + y * (BOTTOM - TOP) / HEIGHT)
        norm = abs(z) ** 2
        for count in xrange(ITERATIONS):
            if norm <= 4.0:
                z = z * z + c
                norm = abs(z * z)
            else:
                break

        (r, g, b) = (count * 6, 0, 0)
        image.put("#%02x%02x%02x" % (r, g, b), (x, y))

        if time.time() > next_update:
            next_update = time.time() + UPDATE_TIME
            root.update()

total_duration = time.time() - start_time
print "duration: %.1fsec, %.1f pixel/sec" % (total_duration, HEIGHT * WIDTH / total_duration)

root.mainloop()