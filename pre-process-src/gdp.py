import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

beijing_df = pd.read_csv("data_with_unit\\beijing.csv")
shanghai_df = pd.read_csv("data_with_unit\\shanghai.csv")
guangzhou_df = pd.read_csv("data_with_unit\\guangzhou.csv")
shenzhen_df = pd.read_csv("data_with_unit\\shenzhen.csv")
quanzhou_df = pd.read_csv("data_with_unit\\quanzhou.csv")

# 计算每个城市的单位面积租金均价
beijing_mean = beijing_df['unit_rent'].mean()
beijing_mean = round(beijing_mean, 2)
shanghai_mean = shanghai_df['unit_rent'].mean()
shanghai_mean = round(shanghai_mean, 2)
guangzhou_mean = guangzhou_df['unit_rent'].mean()
guangzhou_mean = round(guangzhou_mean, 2)
shenzhen_mean = shenzhen_df['unit_rent'].mean()
shenzhen_mean = round(shenzhen_mean, 2)
quanzhou_mean = quanzhou_df['unit_rent'].mean()
quanzhou_mean = round(quanzhou_mean, 2)

# 2021年人均GDP
beijing_gdp = 183937.45
shanghai_gdp = 173756.71
guangzhou_gdp = 151162.22
shenzhen_gdp = 174628.38
quanzhou_gdp = 128715.59

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
city = ['北京', '上海', '广州', '深圳', '泉州']
x = [1, 2, 3, 4, 5]

# 画图，比较人均GDP和单位面积租金的分别
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
gdp = [beijing_gdp, shanghai_gdp, guangzhou_gdp, shenzhen_gdp, quanzhou_gdp]
ax1.bar(x, gdp, 0.5, color='g', tick_label=city)
for a, b in zip(x, gdp):
    ax1.text(a, b, b, ha='center', va='bottom')
ax1.set_title('五个城市人均GDP')
ax1.set_xlabel('城市')
ax1.set_ylabel('人均GDP(元)')

mean = [beijing_mean, shanghai_mean, guangzhou_mean, shenzhen_mean, quanzhou_mean]
plt.bar(x, mean, 0.5, color='c', tick_label=city)
for a, b in zip(x, mean):
    ax2.text(a, b, b, ha='center', va='bottom')
ax2.set_title('五个城市单位面积租金均价')
ax2.set_xlabel('城市')
ax2.set_ylabel('单位面积租金(元/面积)')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
plt.savefig('fig_q6\\五个城市人均GDP和单位面积租金均价分别.png')

# 画图，输出单位面积租金/人均GDP比例
ratio = [round(beijing_mean / beijing_gdp * 1000, 2), round(shanghai_mean / shanghai_gdp * 1000, 2),
         round(guangzhou_mean / guangzhou_gdp * 1000, 2), round(shenzhen_mean / shenzhen_gdp * 1000, 2),
         round(quanzhou_mean / quanzhou_gdp * 1000, 2)]
plt.figure()
plt.bar(x, ratio, 0.5, color='lime', tick_label=city)
for a, b in zip(x, ratio):
    plt.text(a, b, b, ha='center', va='bottom')
plt.title('五个城市单位面积租金和人均GDP占比')
plt.xlabel('城市')
plt.ylabel('比例(千分)')
plt.savefig('fig_q6\\五个城市单位面积租金和人均GDP占比.png')
