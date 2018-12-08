import numpy as np
import sys
from numpy import sin, cos, pi, sqrt
from numpy import arcsin as asin
from numpy import arccos as acos
from numpy import arctan as atan

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# 入力しないといけない値が多すぎる！
# リストを入力値として、関数内で個々の変数を定義すべき！

def fk(l1, l2, l3, th1, th2):
    x2 = l2*cos(th2) - (l1 + l3) *cos(th1)
    y2 = l2*sin(th2) + (l1 + l3) *sin(th1)
    x1 = -l1 * cos(th1)
    y1 = l1 * sin(th1)

    return x1, y1, x2, y2

def fk_frame(l1, l2, l3, l4, l5, l6, l7, th1, th2, x1, y1, x2, y2):
    x3 = - l4 * cos(th2) - l1 * cos(th1)
    y3 = - l4 * sin(th2) + l1 * sin(th1)

    x4 = (l2 + l6) * cos(th2) - (l1 + l3) * cos(th1) - l7 * sin(th2)
    y4 = (l2 + l6) * sin(th2) + (l1 + l3) * sin(th1) + l7 * cos(th2)

    x5 = (l2 + l6) * cos(th2) - (l1 + l3) * cos(th1) + l7 * sin(th2)
    y5 = (l2 + l6) * sin(th2) + (l1 + l3) * sin(th1) - l7 * cos(th2)

    x_f1 = [0, -l4*cos(th2), x3, x1]
    y_f1 = [0, -l4*sin(th2), y3, y1]

    x_f2 = [x3, x1-l5*sin(th2), x2]
    y_f2 = [y3, y1+l5*cos(th2), y2]

    x_l = [x2, x4, x5, x2]
    y_l = [y2, y4, y5, y2]

    return x_f1, y_f1, x_f2, y_f2, x_l, y_l


fig = plt.figure(1)
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-0.4, 0.4), ylim=(-0.1, 0.4))
ax.grid()

# th1 = [pi / 4] * 100
# th2 = np.linspace(- pi / 6, pi / 6, 100)

l1, l2, l3, l4, l5, l6, l7 = 0.18, 0.16, 0.0, 0.05, 0.03, 0.07, 0.07

x0 = np.linspace(0.15, 0.2, 100)
x1 = np.linspace(0.2, 0.2, 100)
y0 = np.linspace(0.15, 0.2, 100)
y1 = np.linspace(0.2, 0.25, 100)

x = np.append(x0, x1)
y = np.append(y0, y1)

ite_len = len(x)

# 90 < th1
th1 = asin((l2*sin(2*atan((2* l2 * y - sqrt(
    -l1 ** 4 - 4 * l1 ** 3 * l3 + 2 * l1 ** 2 * l2 ** 2 - 6 * l1 ** 2 * l3 ** 2 + 2 * l1 ** 2 * x ** 2 + 2 * l1 ** 2 * y ** 2 + 4 * l1 * l2 ** 2 * l3 - 4 * l1 * l3 ** 3 + 4 * l1 * l3 * x ** 2 + 4 * l1 * l3 * y ** 2 - l2 ** 4 + 2 * l2 ** 2 * l3 ** 2 + 2 * l2 ** 2 * x ** 2 + 2 * l2 ** 2 * y ** 2 - l3 ** 4 + 2 * l3 ** 2 * x ** 2 + 2 * l3 ** 2 * y ** 2 - x ** 4 - 2 * x ** 2 * y ** 2 - y ** 4)) / (
                              -l1 ** 2 - 2 * l1 * l3 + l2 ** 2 + 2 * l2 * x - l3 ** 2 + x ** 2 + y ** 2))) - y) / (
           l1 + l3)) + pi
print(th1)
th2 = 2 * atan((2 * l2 * y - sqrt(
    -l1 ** 4 - 4 * l1 ** 3 * l3 + 2 * l1 ** 2 * l2 ** 2 - 6 * l1 ** 2 * l3 ** 2 + 2 * l1 ** 2 * x ** 2 + 2 * l1 ** 2 * y ** 2 + 4 * l1 * l2 ** 2 * l3 - 4 * l1 * l3 ** 3 + 4 * l1 * l3 * x ** 2 + 4 * l1 * l3 * y ** 2 - l2 ** 4 + 2 * l2 ** 2 * l3 ** 2 + 2 * l2 ** 2 * x ** 2 + 2 * l2 ** 2 * y ** 2 - l3 ** 4 + 2 * l3 ** 2 * x ** 2 + 2 * l3 ** 2 * y ** 2 - x ** 4 - 2 * x ** 2 * y ** 2 - y ** 4)) / (
               -l1 ** 2 - 2 * l1 * l3 + l2 ** 2 + 2 * l2 * x - l3 ** 2 + x ** 2 + y ** 2))
print(th2)


#  0 < 90 < th1
# th1 = -asin((l2*sin(2*atan((2*l2*y - sqrt(-l1**4 - 4*l1**3*l3 + 2*l1**2*l2**2 - 6*l1**2*l3**2 + 2*l1**2*x**2 + 2*l1**2*y**2 + 4*l1*l2**2*l3 - 4*l1*l3**3 + 4*l1*l3*x**2 + 4*l1*l3*y**2 - l2**4 + 2*l2**2*l3**2 + 2*l2**2*x**2 + 2*l2**2*y**2 - l3**4 + 2*l3**2*x**2 + 2*l3**2*y**2 - x**4 - 2*x**2*y**2 - y**4))/(-l1**2 - 2*l1*l3 + l2**2 + 2*l2*x - l3**2 + x**2 + y**2))) - y)/(l1 + l3))
# th2 = 2*atan((2*l2*y - sqrt(-l1**4 - 4*l1**3*l3 + 2*l1**2*l2**2 - 6*l1**2*l3**2 + 2*l1**2*x**2 + 2*l1**2*y**2 + 4*l1*l2**2*l3 - 4*l1*l3**3 + 4*l1*l3*x**2 + 4*l1*l3*y**2 - l2**4 + 2*l2**2*l3**2 + 2*l2**2*x**2 + 2*l2**2*y**2 - l3**4 + 2*l3**2*x**2 + 2*l3**2*y**2 - x**4 - 2*x**2*y**2 - y**4))/(-l1**2 - 2*l1*l3 + l2**2 + 2*l2*x - l3**2 + x**2 + y**2))


def two_link(th1, th2):
    l1, l2, l3, l4, l5, l6, l7 = 0.18, 0.16, 0.0, 0.05, 0.03, 0.07, 0.07

    # [th1, th2] = np.radians([110, 15])

    x1, y1, x2, y2 = fk(l1, l2, l3, th1, th2)

    x = [0, x1, x2]
    y = [0, y1, y2]

    x_f1, y_f1, x_f2, y_f2, x_l, y_l = fk_frame(l1, l2, l3, l4, l5, l6, l7, th1, th2, x1, y1, x2, y2)

    return x, y, x_f1, y_f1, x_f2, y_f2, x_l, y_l


xl, yl, x_f1l, y_f1l, x_f2l, y_f2l, x_ll, y_ll = [], [], [], [], [], [], [], []
#初期化している。


for t1, t2 in zip(th1, th2):
    x, y, x_f1, y_f1, x_f2, y_f2, x_l, y_l = two_link(t1, t2)

    xl.append(x)
    yl.append(y)
    x_f1l.append(x_f1)
    y_f1l.append(y_f1)
    x_f2l.append(x_f2)
    y_f2l.append(y_f2)
    x_ll.append(x_l)
    y_ll.append(y_l)

line1, = plt.plot([], [], "-g", lw=5, label="link")
line2, = plt.plot([], [], "-g", lw=5, label="link")
line3, = plt.plot([], [], "-g", lw=5, label="link")
line4, = plt.plot([], [], "-g", lw=5, label="link")
circle1, = plt.plot([], [], "or", lw=5, ms=10, label="joint")
circle2, = plt.plot([], [], "or", lw=5, ms=10, label="joint")
circle3, = plt.plot([], [], "or", lw=5, ms=10, label="joint")
circle4, = plt.plot([], [], "or", lw=5, ms=10, label="joint")


def update(i):
    line1.set_data(xl[i], yl[i])
    line2.set_data(x_f1l[i], y_f1l[i])
    line3.set_data(x_f2l[i], y_f2l[i])
    line4.set_data(x_ll[i], y_ll[i])

    circle1.set_data(xl[i], yl[i])
    circle2.set_data(x_f1l[i], y_f1l[i])
    circle3.set_data(x_f2l[i], y_f2l[i])
    circle4.set_data(x_ll[i], y_ll[i])


ani = animation.FuncAnimation(fig, update, ite_len, blit=False, interval=10, repeat=False)

plt.show()