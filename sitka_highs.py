import csv
import matplotlib.pyplot as plt
filename='data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
#从文件中获取最高温度
    highs=[]
    for row in reader:
        high=int(row[5])
        highs.append(high)

#根据最高温度画图
plt.style.use('classic')
fig,ax=plt.subplots()
ax.plot(highs,c='red')
ax.set_title('2018/7 Daily high',fontsize=24)
ax.set_xlabel('',fontsize=16)
ax.set_ylabel('Tempreture(F)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()
