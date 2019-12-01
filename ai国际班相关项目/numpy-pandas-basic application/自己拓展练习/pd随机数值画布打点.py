import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

#绘图
ts = pd.Series(np.random.randn(1000),
                index=pd.date_range('1/1/2000',periods=1000))
ts = ts.cumsum()
ts.plot()           #指定
df = pd.DataFrame(np.random.randn(1000,4), index=ts.index,
                    columns=['A', 'B', 'C', 'D'])
df = df.cumsum()      #对随机产生的正态数据累积求和
plt.figure()        #定义画布
df.plot()
plt.legend(loc='best',edgecolor='blue')   #设置图例位置
plt.show()
#

#写入excel文件
df.to_excel('foo.xlsx',sheet_name='Sheet1')
#从excel文件读取数据
pd.read_excel('foo.xlsx','Sheet1',index_col=None,na_values=['NA'])
