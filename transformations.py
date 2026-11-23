
import numpy as np

def translate(points, tx, ty):
    matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    return apply_matrix(points, matrix)


def scale(points, sx, sy):
    matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    return apply_matrix(points, matrix)


def rotate(points, angle):
    rad = np.radians(angle)

    matrix = np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad), np.cos(rad), 0],
        [0, 0, 1]
    ])
    return apply_matrix(points, matrix)


def reflect_x(points):
    matrix = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])
    return apply_matrix(points, matrix)


def shear(points, shx, shy):
    matrix = np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ])
    return apply_matrix(points, matrix)


def apply_matrix(points, matrix):
    homogeneous = np.column_stack(
        (points, np.ones(len(points)))
    )
    transformed = (matrix @ homogeneous.T).T
    return transformed[:, :2]
