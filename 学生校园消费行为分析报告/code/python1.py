import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('E:\python数据分析\教程代码实验\data\data2.csv',encoding='gbk')
student=pd.read_csv('E:\python数据分析\教程代码实验\data\data1.csv',encoding='gbk')
#解决图像中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#任务一
data.dropna(inplace=True,axis=1)
data1=data[['CardNo','Date','Money','Type','Dept']]
data2=data1.iloc[(data['Type']=='消费').values,:]
data2['Date']=pd.to_datetime(data2['Date'])
data2['Hour']=data2['Date'].dt.hour
data2=data2[data2['Hour']>6]
data2=data2[data2['Hour']<22]
data4=data2.drop(labels='Hour',axis=1)
student=student[['CardNo','Sex','Major']]
data3=pd.merge(data4,student,on='CardNo')