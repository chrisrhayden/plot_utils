from matplotlib import pyplot as plt
import numpy as np


class Rectangle:
    def __init__(self, x, y, w, h, points=None):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

        if points:
            self.top_points = points[0]
            self.bottom_points = points[1]
            self.left_points = points[2]
            self.right_points = points[3]
        else:
            self.make_points()

    def make_points(self):
        x_points = list(range(self.x1, self.x2 + 1))
        y_points = list(range(self.y1, self.y2 + 1))

        self.top_points = [x_points, [self.y2] * len(x_points)]
        self.bottom_points = [x_points, [self.y1] * len(x_points)]
        self.left_points = [[self.x1] * len(y_points), y_points]
        self.right_points = [[self.x2] * len(y_points), y_points]

    def plot_self(self):
        plt.plot(self.top_points[0], self.top_points[1], marker='o')
        plt.plot(self.bottom_points[0], self.bottom_points[1], marker='o')
        plt.plot(self.left_points[0], self.left_points[1], marker='o')
        plt.plot(self.right_points[0], self.right_points[1], marker='o')

    def multiply_matrix(self, matrix):
        top = matrix.dot(self.top_points)
        bottom = matrix.dot(self.bottom_points)
        left = matrix.dot(self.left_points)
        right = matrix.dot(self.right_points)

        x1 = bottom[0][0]
        y1 = right[1][0]
        x2 = bottom[0][-1]
        y2 = right[1][-1]

        w = x2 - x1
        h = y2 - y1

        return Rectangle(x1, y1, w, h, points=[top, bottom, left, right])

    def __repr__(self):
        return f'Rectangle - x1 = {self.x1} - y1 = {self.y1} ' \
            + f'x2 = {self.x2} - y2 = {self.y2}'


def main():
    m = np.array([[4, 0], [2, 1]])

    r = Rectangle(1, 1, 10, 10)
    R = r.multiply_matrix(m)

    r.plot_self()
    R.plot_self()

    plt.grid(True)
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    main()
