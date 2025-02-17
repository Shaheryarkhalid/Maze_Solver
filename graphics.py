from tkinter import Tk, Canvas, BOTH


class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("First ever tkinter Window")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="green", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = True

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill="red"):
        line.draw(self.canvas, fill_color=fill)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:

    def __init__(self, p1, p2):
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y

    def draw(self, canvas, fill_color="red"):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
