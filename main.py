from cell import Cell
from graphics import Window, Line, Point
from maze import Maze


def main():
    win = Window(800, 600)

    # c1 = Cell(win)
    # c1.has_right_wall = False
    # c1.draw(Point(50, 50), Point(100, 100))
    #
    # c2 = Cell(win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw(Point(100, 50), Point(150, 100))
    #
    # c1.draw_move(c2)
    #
    # c3 = Cell(win)
    # c3.has_top_wall = False
    # c3.has_right_wall = False
    # c3.draw(Point(100, 100), Point(150, 150))
    #
    # c2.draw_move(c3)
    #
    # c4 = Cell(win)
    # c4.has_left_wall = False
    # c4.draw(Point(150, 100), Point(200, 150))
    #
    # c3.draw_move(c4, True)

    maze = Maze(123, 234, 10, 10, 100, 100, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
