import numpy as np
import matplotlib.pyplot as plt
import random


# Flips horizontally numpy tuple (x, y) to return (-x, y)
def hflip(t):
    return np.array([-t[0], t[1]])


# Flips vertically numpy tuple (x, y) to return (x, -y)
def vflip(t):
    return np.array([t[0], -t[1]])


# Generates movement numpy tuples for Peano curve
# n: order of Peano curve
# returns (x, y) with x, y in {-1, 0, 1}
# uses numpy for tuples, so it's easy to do arithmetic with them
def peano_curve(n):
    if n == 0:
        pass
    else:
        tmp = list(peano_curve(n - 1))
        for t in tmp:
            yield t
        yield np.array([ 0,  1])
        for t in tmp:
            yield hflip(t)
        yield np.array([ 0,  1])
        for t in tmp:
            yield t
        yield np.array([ 1,  0])
        for t in tmp:
            yield vflip(t)
        yield np.array([ 0, -1])
        for t in tmp:
            yield -t
        yield np.array([ 0, -1])
        for t in tmp:
            yield vflip(t)
        yield np.array([ 1,  0])
        for t in tmp:
            yield t
        yield np.array([ 0,  1])
        for t in tmp:
            yield hflip(t)
        yield np.array([ 0,  1])
        for t in tmp:
            yield t


# Draw a line from p1 to p2 with matplotlib
# p1, p2: numpy tuples (x, y)
def plt_line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    plt.plot([x1, x2], [y1, y2], 'b')


n = random.randint(1, 4)
plt.figure('Peano Curve')
plt.title('Order {}'.format(n))
plt.axis('off')
point = np.array([0, 0])
for delta in peano_curve(n):
    plt_line(point, point + delta)
    point = point + delta
plt.show()
