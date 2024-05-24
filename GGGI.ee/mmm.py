from win32gui import *
from win32con import *
from random import *

# Функция для рисования прямоугольников с эффектом инверсии
def draw_rects(dc, x, y, w, h, count, dx, dy):
    for i in range(count):
        PatBlt(dc, x + i * dx, y + i * dy, w - 2 * i * dx, h - 2 * i * dy, PATINVERT)


# Основная функция
def main():
    dc = GetDC(0)
    draw_rects(dc, randrange(1920), randrange(1080), 250, 250, 13, 10, 10)

