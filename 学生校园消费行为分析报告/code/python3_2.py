import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

data=pd.read_csv('E:/python数据分析/教程代码实验/data/data2.csv',encoding='gbk')
#任务3.2
new_data_consume=data.groupby('CardNo')['Money'].sum().reset_index()
new_data_card=data.groupby('CardNo')['CardCount'].count().reset_index()
new_data=pd.merge(left=new_data_card,right=new_data_consume,on='CardNo')
# print(new_data.head(1000))
new_data.to_csv('E:/python数据分析/教程代码实验/任务三/result/task3_X1.csv',index=False)

data_values=new_data[['CardCount','Money']].values
#标准化处理数据
model=StandardScaler().fit(data_values)
data_values_ss=model.transform(data_values)
# for k in range(2, 6):
#     model = KMeans(n_clusters=k).fit(data_values_ss)
#     print(k, silhouette_score(data_values_ss, model.labels_))

model=KMeans(n_clusters=4).fit(data_values_ss)
for i in range(4):
    plt.scatter(data_values_ss[model.labels_==i,0],data_values_ss[model.labels_==i,1])
plt.title('聚类模型效果图')
plt.xlabel('刷卡频次')
plt.ylabel('消费金额')
plt.savefig('E:/python数据分析/教程代码实验/任务三/result/消费金额和刷卡频次的聚类模型图')
plt.show()