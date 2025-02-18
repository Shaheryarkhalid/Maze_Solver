from cell import Cell
from graphics import Point
import random, time


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
        self._draw_cells()
        self._reset_cells_visited()

    def _create_cells(self):
        for _ in range(self.num_rows):
            cell_cols = []
            for _ in range(self.num_cols):
                cell_cols.append(Cell(self._win))
            self._cells.append(cell_cols)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False

    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if i > 0 and self._cells[i - 1][j].visited is False:
                possible_directions.append((i - 1, j))
            if i < self.num_rows - 1 and self._cells[i + 1][j].visited is False:
                possible_directions.append((i + 1, j))
            if j > 0 and self._cells[i][j - 1].visited is False:
                possible_directions.append((i, j - 1))
            if j < self.num_cols - 1 and self._cells[i][j + 1].visited is False:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                return
            next_cell = possible_directions[random.randrange(len(possible_directions))]
            if next_cell[0] < i:
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
            if next_cell[0] > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
            if next_cell[1] > j:
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
            if next_cell[1] < j:
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
            self._break_walls(next_cell[0], next_cell[1])

    def _draw_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                point1 = Point(
                    self.x1 + (j * self.cell_size_x), self.y1 + (i * self.cell_size_y)
                )
                point2 = Point(point1.x + self.cell_size_x, point1.y + self.cell_size_y)
                self._cells[i][j].draw(point1, point2)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._cells[i][j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        if (
            i > 0
            and self._cells[i][j].has_top_wall is False
            and self._cells[i - 1][j].visited is False
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self.num_rows - 1
            and self._cells[i][j].has_bottom_wall is False
            and self._cells[i + 1][j].visited is False
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if (
            j > 0
            and self._cells[i][j].has_left_wall is False
            and self._cells[i][j - 1].visited is False
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        if (
            j < self.num_cols - 1
            and self._cells[i][j].has_right_wall is False
            and self._cells[i][j + 1].visited is False
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        self._animate()
        return False


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.5)
