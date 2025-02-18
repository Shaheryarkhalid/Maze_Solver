from graphics import Line, Point


class Cell:

    def __init__(self, win=None):
        self.visited = False
        self.drawn = False
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self.has_left_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, p1, p2):
        if self._win is None:
            return
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        self.draw_top_wall()
        self.draw_bottom_wall()
        self.draw_right_wall()
        self.draw_left_wall()

    def draw_top_wall(self):
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)

    def draw_bottom_wall(self):
        if self.has_bottom_wall:
            line = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
            self._win.draw_line(line)

    def draw_left_wall(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)

    def draw_right_wall(self):
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        fill_color = "white"
        if undo:
            fill_color = "gray"

        self_cell_half_height = (max(self._x1, self._x2) - min(self._x1, self._x2)) // 2
        self_cell_half_width = (max(self._y1, self._y2) - min(self._y1, self._y2)) // 2

        to_cell_half_height = (
            max(to_cell._x1, to_cell._x2) - min(to_cell._x1, to_cell._x2)
        ) // 2
        to_cell_half_width = (
            max(to_cell._y1, to_cell._y2) - min(to_cell._y1, to_cell._y2)
        ) // 2

        line = Line(
            Point(
                min(self._x1, self._x2) + self_cell_half_width,
                min(self._y1, self._y2) + self_cell_half_height,
            ),
            Point(
                min(to_cell._x1, to_cell._x2) + to_cell_half_width,
                min(to_cell._y1, to_cell._y2) + to_cell_half_height,
            ),
        )
        self._win.draw_line(line, fill=fill_color)
