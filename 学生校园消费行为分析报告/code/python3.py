#任务3
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

data=pd.read_csv('E:/python数据分析/教程代码实验/任务二/result/task2_X1.csv')

#任务3.1
#计算出学生的人数
stuNum=data['CardNo'].nunique()
#计算学生消费的总额
stuCon=data['Money'].sum()
#计算出学生总的人均刷卡频数和消费金额
ave=data['CardNo'].count()/stuNum
con=stuCon/stuNum
plt.title('本月的人均刷卡频数和消费金额直方图')
plt.bar(range(1, 3), [ave,con], width=0.5)
plt.xticks(range(1, 3), ['本月人均刷卡次数','本月的人均消费金额'])
plt.savefig(fname = 'E:/python数据分析/教程代码实验/任务三/result/本月直线方图')
plt.show()
plt.close()
#计算不同专业的不同性别人均消费
data1=data.groupby(['Sex','Major'])
sum1=data1['Money'].sum()
sum2=data1['Money'].count()
num1=data1['CardNo'].nunique()
# data2=data1.get_group(('女'))
data3=sum1/num1
data4=sum2/num1
#取出专业的名称
titles=data3.index
for i in range(0,40):
    plt.title(titles[i][1]+'男女直方图')
    plt.bar(range(1, 5), [data3[i], data3[i+39],data4[i], data4[i+39]], width=0.5)
    plt.xticks(range(1, 5), [titles[i][0]+'平均消费值', titles[i+39][0]+'平均消费值',titles[i][0]+'平均刷卡频次', titles[i+39][0]+'平均刷卡频次'])
    s=str(i)
    plt.savefig(fname = 'E:/python数据分析/教程代码实验/任务三/result/'+s+'.png')
    plt.close()
