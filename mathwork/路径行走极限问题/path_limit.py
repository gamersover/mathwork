# -*- coding: utf-8 -*-
'''
在笛卡尔直角坐标系xOy中，有点A(0,1)，OA作为起始向量，从点A出发，到达目的地点B，点B满足：
(1)AB向量与前一个向量OA的夹角为theta（0<=theta<=π）；
(2)AB即行走的距离是前一个距离OA的beta（0<=beta<=1）倍；
下一次行走以向量AB为基准行走至下一目的地，依此类推。

当beta=1, theta=2*pi/n时，所得的图像为正n边形
当beta=1, theta=pi*a, a越接近于0，图像内圆和外圆接近，a接近1，图像内圆半径接近为0
''' 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import math

beta = 1
# a = np.random.uniform(0,1)
# print(a)
a = 2/7
theta = math.pi*a


def data_gen(): 
    t = 0
    x = 0
    y = 0 
    while t < 200:
        x += pow(beta, t)*math.sin(t*theta)
        y += pow(beta, t)*math.cos(t*theta)
        t += 1
        if t == 200:
            print(x,y)
        yield x, y

fig, ax = plt.subplots() 
line, = ax.plot([], [], lw=2)
if beta == 1:
    ax.set_ylim(-math.pi/theta, math.pi/theta) 
    ax.set_xlim(-math.pi/theta, math.pi/theta)
else:
    ax.set_ylim(-1/(1-beta), 1/(1-beta))
    ax.set_xlim(-beta/(1-beta), beta/(1-beta)) 
ax.grid() 
xdata, ydata = [], [] 
def run(data): 
    x,y = data 
    xdata.append(x) 
    ydata.append(y) 
    # ax.set_xlim(x/2, x)
    # ax.set_ylim(x/2, x)
    # ax.figure.canvas.draw() 
    line.set_data(xdata, ydata) 
    return line, 
ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=100, 
  repeat=False) 
plt.show() 