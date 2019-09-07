import numpy as np
import matplotlib.pyplot as plt
import random


# Flips numpy tuple (x, y) to return (y, x)
def flip(t):
    return np.array([t[1], t[0]])


# Generates movement numpy tuples for Hilbert curve
# n: order of Hilbert Hilbert curve
# returns (x, y) with x, y in {-1, 0, 1}
# uses numpy for tuples, so it's easy to do arithmetic with them
def hilbert_curve(n):
    if n == 0:
        pass
    else:
        # it's a little bit annoying that I can't yield from
        # another generator but transform the output
        tmp = list(hilbert_curve(n - 1))
        for t in tmp:
            yield flip(t)
        yield np.array([ 0,  1])
        # don't do: yield from hilbert_curve(n - 1)
        # because we already have done that exhaustively
        for t in tmp:
            yield t
        yield np.array([ 1,  0])
        for t in tmp:
            yield t
        yield np.array([ 0, -1])
        for t in tmp:
            yield -flip(t)


# Draw a line from p1 to p2 with matplotlib
# p1, p2: numpy tuples (x, y)
def plt_line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    plt.plot([x1, x2], [y1, y2], 'b')


n = random.randint(1, 6)
plt.figure('Hilbert Curve')
plt.title('Order {}'.format(n))
plt.axis('off')
point = np.array([0, 0])
for delta in hilbert_curve(n):
    plt_line(point, point + delta)
    point = point + delta
plt.show()
