import unittest
from maze import Maze


class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_cols(self):
        num_cols = 23
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)

    def test_break_entrance_and_exit(self):
        maze = Maze(0, 0, 10, 10, 10, 10)
        self.assertEqual(maze._cells[0][0].has_right_wall, False)
        self.assertEqual(maze._cells[9][9].has_left_wall, False)

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 10, 10, 10, 10)
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):
                self.assertEqual(maze._cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
