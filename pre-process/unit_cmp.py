import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

beijing_df = pd.read_csv("data_with_unit\\beijing.csv")
shanghai_df = pd.read_csv("data_with_unit\\shanghai.csv")
guangzhou_df = pd.read_csv("data_with_unit\\guangzhou.csv")
shenzhen_df = pd.read_csv("data_with_unit\\shenzhen.csv")
quanzhou_df = pd.read_csv("data_with_unit\\quanzhou.csv")

# 计算均价、最大值、最小值、中位数，取小数点后两位
beijing_mean = beijing_df['unit_rent'].mean()
beijing_mean = round(beijing_mean, 2)
beijing_high = beijing_df['unit_rent'].max()
beijing_low = beijing_df['unit_rent'].min()
beijing_mid = beijing_df['unit_rent'].median()
beijing_mid = round(beijing_mid, 2)

shanghai_mean = shanghai_df['unit_rent'].mean()
shanghai_mean = round(shanghai_mean, 2)
shanghai_high = shanghai_df['unit_rent'].max()
shanghai_low = shanghai_df['unit_rent'].min()
shanghai_mid = shanghai_df['unit_rent'].median()
shanghai_mid = round(shanghai_mid, 2)

guangzhou_mean = guangzhou_df['unit_rent'].mean()
guangzhou_mean = round(guangzhou_mean, 2)
guangzhou_high = guangzhou_df['unit_rent'].max()
guangzhou_low = guangzhou_df['unit_rent'].min()
guangzhou_mid = guangzhou_df['unit_rent'].median()
guangzhou_mid = round(guangzhou_mid, 2)

shenzhen_mean = shenzhen_df['unit_rent'].mean()
shenzhen_mean = round(shenzhen_mean, 2)
shenzhen_high = shenzhen_df['unit_rent'].max()
shenzhen_low = shenzhen_df['unit_rent'].min()
shenzhen_mid = shenzhen_df['unit_rent'].median()
shenzhen_mid = round(shenzhen_mid, 2)

quanzhou_mean = quanzhou_df['unit_rent'].mean()
quanzhou_mean = round(quanzhou_mean, 2)
quanzhou_high = quanzhou_df['unit_rent'].max()
quanzhou_low = quanzhou_df['unit_rent'].min()
quanzhou_mid = quanzhou_df['unit_rent'].median()
quanzhou_mid = round(quanzhou_mid, 2)

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
city = ['北京', '上海', '广州', '深圳', '泉州']   # x刻度标签
x = [1, 2, 3, 4, 5]                           # x坐标
# 按最小值、最大值、均价和中位数画四张图
low = [beijing_low, shanghai_low, guangzhou_low, shenzhen_low, quanzhou_low]
mean = [beijing_mean, shanghai_mean, guangzhou_mean, shenzhen_mean, quanzhou_mean]
mid = [beijing_mid, shanghai_mid, guangzhou_mid, shenzhen_mid, quanzhou_mid]
high = [beijing_high, shanghai_high, guangzhou_high, shenzhen_high, quanzhou_high]

plt.figure()
plt.bar(x, low, 0.5, color='r', tick_label=city)
for a, b in zip(x, low):
    plt.text(a, b+0.2, b, ha='center', va='bottom')
plt.title('五个城市单位面积租金最低价')
plt.xlabel('城市')
plt.ylabel('单位面积租金最低价(元/面积)')
plt.savefig('fig_q2\\五个城市单位面积租金最低价.png')

plt.figure()
plt.bar(x, mean, 0.5, color='b', tick_label=city)
for a, b in zip(x, mean):
    plt.text(a, b+0.2, b, ha='center', va='bottom')
plt.title('五个城市单位面积租金均价')
plt.xlabel('城市')
plt.ylabel('单位面积租金均价(元/面积)')
plt.savefig('fig_q2\\五个城市单位面积租金均价.png')

plt.figure()
plt.bar(x, mid, 0.5, color='y', tick_label=city)
for a, b in zip(x, mid):
    plt.text(a, b+0.2, b, ha='center', va='bottom')
plt.title('五个城市单位面积租金中位数')
plt.xlabel('城市')
plt.ylabel('单位面积租金中位数(元/面积)')
plt.savefig('fig_q2\\五个城市单位面积租金中位数.png')

plt.figure()
plt.bar(x, high, 0.5, color='g', tick_label=city)
for a, b in zip(x, high):
    plt.text(a, b+0.2, b, ha='center', va='bottom')
plt.title('五个城市单位面积租金最高价')
plt.xlabel('城市')
plt.ylabel('单位面积租金最高价(元/面积)')
plt.savefig('fig_q2\\五个城市单位面积租金最高价.png')
