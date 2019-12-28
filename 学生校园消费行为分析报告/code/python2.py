import pandas as pd
import matplotlib.pyplot as plt
#解决图像中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#任务二
data3=pd.read_csv('E:/python数据分析/教程代码实验/任务一/result/task1_1_X.csv',encoding='gbk')
#对数据进行就餐地点的筛选
def canteen_filter(all_data):
    data=[]
    canteens=['第一食堂','第二食堂','第三食堂','第四食堂','第五食堂','教师食堂']
    for i in canteens:
        data.append(all_data.loc[all_data['Dept']==i])
    return data
#添加一列tab值标记就餐人数
data3['tab']=1
#统计data3的行数
count = len(data3)
#对时间进行排序
data3.sort_index(by='Date',ascending=True,inplace=True)
# print(data3.iloc[(data3['Dept']=='第一食堂').values,:]['tab'].sum())
# print(abs(data3['Date'].iloc[1]-data3['Date'].iloc[0]).total_seconds())
# 统计就餐人数
for i in range(1,count):
    if data3['CardNo'].iloc[i] == data3['CardNo'].iloc[i-1]:
        temp = abs(data3['Date'].iloc[i]-data3['Date'].iloc[i-1]).total_seconds()
        if temp<600:
            data3['tab'].iloc[i]=0
data3.to_csv('E:/python数据分析/教程代码实验/任务二/result/task2_X1.csv',index=False)
data4=pd.read_csv('E:/python数据分析/教程代码实验/任务二/result/task2_X1.csv')
#划分早中晚的时间
data4['Date']=pd.to_datetime(data4['Date'])
data4['Hour']=data4['Date'].dt.hour
# #早餐
dataMon=data4.iloc[(data4['Hour']>=7).values,:]
dataMon=dataMon.iloc[(dataMon['Hour']<=10).values,:]
dataMon.to_csv('E:/python数据分析/教程代码实验/任务二/result/task2_X2.csv',index=False)
#中午餐
dataNon=data4.iloc[(data4['Hour']>=11).values,:]
dataNon=dataNon.iloc[(dataNon['Hour']<=16).values,:]
dataNon.to_csv('E:/python数据分析/教程代码实验/任务二/result/task2_X3.csv',index=False)
#晚餐
dataNig=data4.iloc[(data4['Hour']>=17).values,:]
dataNig=dataNig.iloc[(dataNig['Hour']<=21).values,:]
dataNig.to_csv('E:/python数据分析/教程代码实验/任务二/result/task2_X4.csv',index=False)
Depts=['第一食堂','第二食堂','第三食堂','第四食堂','第五食堂']
#分别存储早中晚的就餐地点人数
nums=[]
nums2=[]
nums3=[]
for i in Depts:
    nums.append(dataMon.iloc[(dataMon['Dept']==i).values,:]['tab'].sum())
    nums2.append(dataNon.iloc[(dataNon['Dept']==i).values,:]['tab'].sum())
    nums3.append(dataNig.iloc[(dataNig['Dept'] == i).values, :]['tab'].sum())
plt.title('早餐饼图')
plt.pie(nums, labels=['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂'] ,autopct='%.2f %%')
plt.savefig('E:/python数据分析/教程代码实验/任务二/result/早餐饼图.png')
plt.close()
plt.title('中午餐饼图')
plt.pie(nums2, labels=['第一食堂', '第二食堂', '第三食堂', '第四食堂', '第五食堂'],autopct='%.2f %%')
plt.savefig('E:/python数据分析/教程代码实验/任务二/result/中午餐饼图.png')
plt.close()
plt.title('晚餐饼图')
plt.pie(nums3,labels=['第一食堂','第二食堂','第三食堂','第四食堂','第五食堂'],autopct='%.2f %%')
plt.savefig('E:/python数据分析/教程代码实验/任务二/result/晚餐饼图.png')
plt.close()
# plt.show()
#提取天数和星期
data4['Week']=data4['Date'].apply(lambda x:x.weekday()+1)
data4['Day']=[i.day for i in data4['Date']]
#绘制非工作日折线图
#提取非工作日的数据
unworkday_data1=data4.loc[data4['Day']==5]
unworkday_data2=data4.loc[data4['Day']!=28]
unworkday_data2=unworkday_data2.loc[data4['Week']>5]
unworkday_data=pd.concat([unworkday_data1,unworkday_data2])
#非工作日的天数
unworkday_num=unworkday_data.groupby('Day')['Day'].nunique().sum()
#进行数据筛选
unworkday_data3=canteen_filter(unworkday_data)
hours_sum=[]
for i in unworkday_data3:
    #计算小时的就餐频数
    hour_sum=[]
    for j in range(0,24):
        temp=i[i['tab']==1]
        temp=temp[temp['Hour']==j]
        hour_sum.append(temp['tab'].sum())
    hours_sum.append(hour_sum)
#绘制食堂非工作日均曲线图
x=range(0,24)
y1=[y/unworkday_num for y in hours_sum[0]]
y2=[y/unworkday_num for y in hours_sum[1]]
y3=[y/unworkday_num for y in hours_sum[2]]
y4=[y/unworkday_num for y in hours_sum[3]]
y5=[y/unworkday_num for y in hours_sum[4]]
y6=[y/unworkday_num for y in hours_sum[5]]
plt.title('食堂非工作日就餐折线图')
plt.xlabel('时间/小时')
plt.ylabel('日平均就餐人次')
plt.xticks(x)
plt.plot(x,y1,label='第一食堂')
plt.plot(x,y2,label='第二食堂')
plt.plot(x,y3,label='第三食堂')
plt.plot(x,y4,label='第四食堂')
plt.plot(x,y5,label='第五食堂')
plt.plot(x,y6,label='教师食堂')
plt.legend()
plt.savefig('E:/python数据分析/教程代码实验/任务二/result//食堂非工作日就餐折线图.png')
plt.close()

#绘制工作日的折线图
workday_data1=data4.loc[data4['Day']==28]
workday_data2=data4.loc[data4['Day']!=5]
workday_data2=workday_data2.loc[workday_data2['Week']<=5]
workday_data=pd.concat([workday_data1,workday_data2])
#工作日的天数
workday_num=workday_data.groupby('Day')['Day'].nunique().sum()
#进行数据筛选
workday_data3=canteen_filter(workday_data)
hours_sum=[]
for i in workday_data3:
    #计算小时的就餐频数
    hour_sum=[]
    for j in range(0,24):
        temp=i[i['tab']==1]
        temp=temp[temp['Hour']==j]
        hour_sum.append(temp['tab'].sum())
    hours_sum.append(hour_sum)
#绘制食堂非工作日均曲线图
x=range(0,24)
y1=[y/workday_num for y in hours_sum[0]]
#print(y1)
y2=[y/workday_num for y in hours_sum[1]]
y3=[y/workday_num for y in hours_sum[2]]
y4=[y/workday_num for y in hours_sum[3]]
y5=[y/workday_num for y in hours_sum[4]]
y6=[y/workday_num for y in hours_sum[5]]
plt.title('食堂工作日就餐折线图')
plt.xlabel('时间/小时')
plt.ylabel('日平均就餐人次')
plt.xticks(x)
plt.plot(x,y1,label='第一食堂')
plt.plot(x,y2,label='第二食堂')
plt.plot(x,y3,label='第三食堂')
plt.plot(x,y4,label='第四食堂')
plt.plot(x,y5,label='第五食堂')
plt.plot(x,y6,label='教师食堂')
plt.legend()
plt.savefig('E:/python数据分析/教程代码实验/任务二/result//食堂工作日就餐折线图.png')
plt.close()

#绘制食堂日均曲线图
days=data4.groupby('Day')['Day'].nunique().sum()
days2=canteen_filter(data4)
hours_sum=[]
for i in days2:
    #计算小时的就餐频数
    hour_sum=[]
    for j in range(0,24):
        temp=i[i['tab']==1]
        temp=temp[temp['Hour']==j]
        hour_sum.append(temp['tab'].sum())
    hours_sum.append(hour_sum)
x=range(0,24)
y1=[y/days for y in hours_sum[0]]
y2=[y/days for y in hours_sum[1]]
y3=[y/days for y in hours_sum[2]]
y4=[y/days for y in hours_sum[3]]
y5=[y/days for y in hours_sum[4]]
plt.title('食堂就餐折线图')
plt.xlabel('时间/小时')
plt.ylabel('日平均就餐人次')
plt.xticks(x)
plt.plot(x,y1,label='第一食堂')
plt.plot(x,y2,label='第二食堂')
plt.plot(x,y3,label='第三食堂')
plt.plot(x,y4,label='第四食堂')
plt.plot(x,y5,label='第五食堂')
plt.legend()
plt.savefig('E:/python数据分析/教程代码实验/任务二/result//食堂就餐折线图.png')
plt.show()