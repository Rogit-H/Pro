import pandas as pd
inputfile = 'principal_component.xls'
outputfile = 'dimention_reducted.xls'

data = pd.read_excel(inputfile)

from sklearn.decomposition import PCA
pca = PCA(3)                        #保留主成分个数
pca.fit(data)
low_d = pca.transform(data)         #降低维度
pd.DataFrame(low_d).to_excel(outputfile)   #输出文件
pca.inverse_transform(low_d)        #恢复原始数据
