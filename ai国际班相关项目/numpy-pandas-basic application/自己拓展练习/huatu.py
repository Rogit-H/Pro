import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


####2×2的画布
# fig = plt.figure()
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)

####设置画布ax1参数
# ax1.set(xlim=[0.5,4.5],ylim=[-2,8],title='An Example Axes',
#         ylabel='Y-Axis',xlabel='X-Axis')

####x,y曲线函数
# x = np.linspace(0,np.pi)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

####散点图
# x = np.arange(10)
# y = np.random.randn(10)
# plt.scatter(x, y, color='red', marker='+')

####打印图片
# ax1.plot(x,y_sin)
# ax2.plot(x,y_cos)
# ax4.plot(x,y)

####饼图
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
fig, (ax1,ax2) = plt.subplots(2)
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
ax1.axis('equal')
ax2.pie(sizes, autopct='%1.2f%%', shadow=True, startangle=90, explode=explode, pctdistance=1.12)
ax2.axis('equal')
ax2.legend(labels=labels, loc='upper right')

####箱形图
# fig, (ax1, ax2) = plt.subplots(2)
# ax1.boxplot(data)
# ax2.boxplot(data2, vert=False)

####泡泡图
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30* np.random.rand(N))**2 
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.show()