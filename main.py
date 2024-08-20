from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 125, 125)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(135, 135, 225, 225)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(245, 245, 300, 300)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(350, 350, 500, 500)

    win.wait_for_close()


main()