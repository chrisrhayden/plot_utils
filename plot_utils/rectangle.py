from matplotlib import pyplot as plt


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        self.top_points = list()
        self.bottom_points = list()
        self.left_points = list()
        self.right_points = list()

        self.make_points()

    def make_points(self):
        x_points = list(range(self.x1, self.x2))
        y_points = list(range(self.y1, self.y2))

        self.top_points = [x_points, [self.y2] * len(x_points)]
        self.bottom_points = [x_points, [self.y1] * len(x_points)]
        self.left_points = [[self.x1] * len(y_points), y_points]
        self.right_points = [[self.x2] * len(y_points), y_points]

    def multiply_matrix(self, matrix):
        self.top_points = matrix.dot(self.top_points)
        self.bottom_points = matrix.dot(self.bottom_points)
        self.left_points = matrix.dot(self.left_points)
        self.right_points = matrix.dot(self.right_points)

    def __repr__(self):
        return f'Rectangle - x1 = {self.x1} - y1 = {self.y1} ' \
            + f'x2 = {self.x2} - y2 = {self.y2}'

    def plot_self(self):
        plt.plot(self.top_points[0], self.top_points[1], marker='o')
        plt.plot(self.bottom_points[0], self.bottom_points[1], marker='o')
        plt.plot(self.left_points[0], self.left_points[1], marker='o')
        plt.plot(self.right_points[0], self.right_points[1], marker='o')

    def rect_from_matrix(cls, top, bottom, left, right):
        cls.x1 = bottom[0][0]
        cls.y1 = right[1][0]
        cls.x2 = bottom[0][-1]
        cls.y2 = right[1][-1]

        cls.top_points = top
        cls.bottom_points = bottom
        cls.left_points = left
        cls.right_points = right
        return cls
