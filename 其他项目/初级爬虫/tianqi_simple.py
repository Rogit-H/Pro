
import pandas as pd

url2 = 'http://www.tianqihoubao.com/weather/top/zhuhai.html'
links = []

links.insert(0, url2)

df2 = pd.DataFrame()  # creates a new dataframe that's empty

for url in links:
    # 利用pandas获取数据，需要安装 html5lib模块
    dfs = pd.read_html(url, header=-2, encoding='GBK')
    for df in dfs:
        df2= df2.append(df, ignore_index=True)

df2.to_excel('Awd.xlsx',encoding='utf_8_sig',header=-1,index=0) # 将数据存储在excel文件里
#df2.to_csv('MktDataBJ-1.csv',mode='a',encoding='utf_8_sig',header=0,index=0)  # 将数据存储在csv文件里