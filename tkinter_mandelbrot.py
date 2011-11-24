#!/usr/bin/env python
# coding: utf-8

import time
import Tkinter as tkinter


class Mandelbrot(object):
    def __init__(self, width=320, height=240, iterations=20, update_time=0.5):
        self.width = width
        self.height = height
        self.iterations = iterations
        self.update_time = update_time

        self.left = -2
        self.right = 0.5
        self.top = 1.25
        self.bottom = -1.25

    def render(self):
        self.start_time = time.time()
        next_update = self.start_time + self.update_time
        for y in xrange(self.height):
            if time.time() > next_update:
                now = time.time()
                next_update = now + self.update_time
                self.update(now, y)

            for x in xrange(self.width):
                z = complex(0, 0)
                c = complex(self.left + x * (self.right - self.left) / self.width, self.top + y * (self.bottom - self.top) / self.height)
                norm = abs(z) ** 2
                for count in xrange(self.iterations):
                    if norm <= 4.0:
                        z = z * z + c
                        norm = abs(z * z)
                    else:
                        break

                    self.create_pixel(x, y, count, norm)

        self.update(time.time(), self.height)

    def create_pixel(self, x, y, count, norm):
        raise NotImplemented

    def update(self, y):
        raise NotImplemented


class TkMandelbrot(Mandelbrot):
    def __init__(self, *args, **kwargs):
        super(TkMandelbrot, self).__init__(*args, **kwargs)
        self.root = tkinter.Tk()
        self.image = tkinter.PhotoImage(width=self.width, height=self.height)
        lb1 = tkinter.Label(self.root, image=self.image)
        lb1.pack()

    def create_pixel(self, x, y, count, norm):
        (r, g, b) = (count * 6, 0, 0)
        self.image.put("#%02x%02x%02x" % (r, g, b), (x, y))

    def update(self, now, y):
        percent = float(y) / self.height * 100
        duration = now - self.start_time
        print "%.1f%% - duration: %.1fsec" % (percent, duration)
        self.root.update()


if __name__ == '__main__':
    m = TkMandelbrot()
    m.render()
    m.root.mainloop()

