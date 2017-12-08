# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import math

beta = 1
# a = np.random.uniform(0,1)
# print(a)
a = 2/7
theta = math.pi*a

#生成每次行走时的坐标
def path_gen(): 
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

#使用plt画出行走时的动态图
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

ani = animation.FuncAnimation(fig, run, path_gen, blit=True, interval=100, 
  repeat=False) 

plt.show() 