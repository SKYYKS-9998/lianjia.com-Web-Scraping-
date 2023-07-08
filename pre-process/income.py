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

# 五个城市人均收入
beijing_income = 6906
shanghai_income = 6378
guangzhou_income = 4811
shenzhen_income = 5199
quanzhou_income = 3311

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
city = ['北京', '上海', '广州', '深圳', '泉州']
x = [1, 2, 3, 4, 5]

# 画图，比较平均收入和单位面积租金的分别
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
gdp = [beijing_income, shanghai_income, guangzhou_income, shenzhen_income, quanzhou_income]
ax1.bar(x, gdp, 0.5, color='g', tick_label=city)
for a, b in zip(x, gdp):
    ax1.text(a, b, b, ha='center', va='bottom')
ax1.set_title('五个城市平均收入(元)')
ax1.set_xlabel('城市')
ax1.set_ylabel('平均收入(元)')

mean = [beijing_mean, shanghai_mean, guangzhou_mean, shenzhen_mean, quanzhou_mean]
plt.bar(x, mean, 0.5, color='c', tick_label=city)
for a, b in zip(x, mean):
    ax2.text(a, b, b, ha='center', va='bottom')
ax2.set_title('五个城市单位面积租金均价')
ax2.set_xlabel('城市')
ax2.set_ylabel('单位面积租金(元/面积)')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
plt.savefig('fig_q6\\五个城市平均收入和单位面积租金均价分别.png')


# 画图，输出单位面积租金/人均收入比例
ratio = [round(beijing_mean / beijing_income * 1000, 2), round(shanghai_mean / shanghai_income * 1000, 2),
         round(guangzhou_mean / guangzhou_income * 1000, 2), round(shenzhen_mean / shenzhen_income * 1000, 2),
         round(quanzhou_mean / quanzhou_income * 1000, 2)]
plt.figure()
plt.bar(x, ratio, 0.5, color='lime', tick_label=city)
for a, b in zip(x, ratio):
    plt.text(a, b, b, ha='center', va='bottom')
plt.title('五个城市单位面积租金和平均收入占比')
plt.xlabel('城市')
plt.ylabel('比例(百分)')
plt.savefig('fig_q6\\五个城市单位面积租金和平均收入占比.png')
