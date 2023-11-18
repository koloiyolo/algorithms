import numpy as np


def euclidean_distance(point1, point2):
    sums = 0
    for val1, val2 in zip(point1, point2):
        dif = val1 - val2
        sums += dif * dif
    return np.sqrt(sums)


def x_y_min(data):
    x, y = data[0]
    for elem in data:
        if elem[0] < x:
            x = elem[0]

        if elem[1] < y:
            y = elem[1]

    return [x, y]


def x_y_max(data):
    x, y = data[0]
    for elem in data:
        if elem[0] > x:
            x = elem[0]

        if elem[1] > y:
            y = elem[1]

    return [x, y]


def means(data):
    sums = 0
    count = 0
    for elem in data:
        count = count + 1
        sums += elem

    return sums / count

