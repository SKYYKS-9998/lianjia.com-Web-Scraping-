import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def get_stat(room_num):  # 计算最小值、最大值、均价和中位数
    room_low = [[beijing_room_dict[room_num]['rent'].min(), shanghai_room_dict[room_num]['rent'].min(),
                 guangzhou_room_dict[room_num]['rent'].min(), shenzhen_room_dict[room_num]['rent'].min(),
                 quanzhou_room_dict[room_num]['rent'].min()],
                [beijing_room_dict[room_num]['unit_rent'].min(), shanghai_room_dict[room_num]['unit_rent'].min(),
                 guangzhou_room_dict[room_num]['unit_rent'].min(), shenzhen_room_dict[room_num]['unit_rent'].min(),
                 quanzhou_room_dict[room_num]['unit_rent'].min()]]
    room_high = [[beijing_room_dict[room_num]['rent'].max(), shanghai_room_dict[room_num]['rent'].max(),
                  guangzhou_room_dict[room_num]['rent'].max(), shenzhen_room_dict[room_num]['rent'].max(),
                  quanzhou_room_dict[room_num]['rent'].max()],
                 [beijing_room_dict[room_num]['unit_rent'].max(), shanghai_room_dict[room_num]['unit_rent'].max(),
                  guangzhou_room_dict[room_num]['unit_rent'].max(), shenzhen_room_dict[room_num]['unit_rent'].max(),
                  quanzhou_room_dict[room_num]['unit_rent'].max()]]
    room_mean = [[round(beijing_room_dict[room_num]['rent'].mean(), 2),
                  round(shanghai_room_dict[room_num]['rent'].mean(), 2),
                  round(guangzhou_room_dict[room_num]['rent'].mean(), 2),
                  round(shenzhen_room_dict[room_num]['rent'].mean(), 2),
                  round(quanzhou_room_dict[room_num]['rent'].mean(), 2)],
                 [round(beijing_room_dict[room_num]['unit_rent'].mean(), 2),
                  round(shanghai_room_dict[room_num]['unit_rent'].mean(), 2),
                  round(guangzhou_room_dict[room_num]['unit_rent'].mean(), 2),
                  round(shenzhen_room_dict[room_num]['unit_rent'].mean(), 2),
                  round(quanzhou_room_dict[room_num]['unit_rent'].mean(), 2)]]
    room_mid = [[round(beijing_room_dict[room_num]['rent'].median(), 2),
                 round(shanghai_room_dict[room_num]['rent'].median(), 2),
                 round(guangzhou_room_dict[room_num]['rent'].median(), 2),
                 round(shenzhen_room_dict[room_num]['rent'].median(), 2),
                 round(quanzhou_room_dict[room_num]['rent'].median(), 2)],
                [round(beijing_room_dict[room_num]['unit_rent'].median(), 2),
                 round(shanghai_room_dict[room_num]['unit_rent'].median(), 2),
                 round(guangzhou_room_dict[room_num]['unit_rent'].median(), 2),
                 round(shenzhen_room_dict[room_num]['unit_rent'].median(), 2),
                 round(quanzhou_room_dict[room_num]['unit_rent'].median(), 2)]]
    return room_low, room_high, room_mean, room_mid


def plot_graph(graph_type, data1, data2, data3):    # 画图函数
    unit = ''
    title = ''
    # 根据要画的图的类型，设置标题和单元
    if graph_type < 5:
        unit = '(元)'
        if graph_type == 1:
            title = '租金最低价'
        elif graph_type == 2:
            title = '租金最高价'
        elif graph_type == 3:
            title = '租金均价'
        elif graph_type == 4:
            title = '租金中位数'
    else:
        unit = '(元/面积)'
        if graph_type == 5:
            title = '单位面积租金最低价'
        elif graph_type == 6:
            title = '单位面积租金最高价'
        elif graph_type == 7:
            title = '单位面积租金均价'
        elif graph_type == 8:
            title = '单位面积租金中位数'
    plt.figure()
    plt.bar(x - 0.3, data1, 0.3, color='lime')
    plt.bar(x, data2, 0.3, color='yellow', tick_label=city)
    plt.bar(x + 0.3, data3, 0.3, color='c')
    for a, b in zip(x, data1):
        plt.text(a - 0.3, b + 0.2, b, ha='center', va='bottom')
    for a, b in zip(x, data2):
        plt.text(a, b + 0.2, b, ha='center', va='bottom')
    for a, b in zip(x, data3):
        plt.text(a + 0.3, b + 0.2, b, ha='center', va='bottom')
    plt.title('五个城市' + title)
    plt.xlabel('城市')
    plt.ylabel(title + unit)
    plt.legend(room, loc='upper right')
    plt.savefig('fig_q3\\五个城市' + title + '.png')


beijing_df = pd.read_csv("data_with_unit\\beijing.csv")
shanghai_df = pd.read_csv("data_with_unit\\shanghai.csv")
guangzhou_df = pd.read_csv("data_with_unit\\guangzhou.csv")
shenzhen_df = pd.read_csv("data_with_unit\\shenzhen.csv")
quanzhou_df = pd.read_csv("data_with_unit\\quanzhou.csv")

# 只需要居数、租金和单位面积租金的数据
beijing_room = beijing_df[['room', 'rent', 'unit_rent']]
shanghai_room = shanghai_df[['room', 'rent', 'unit_rent']]
guangzhou_room = guangzhou_df[['room', 'rent', 'unit_rent']]
shenzhen_room = shenzhen_df[['room', 'rent', 'unit_rent']]
quanzhou_room = quanzhou_df[['room', 'rent', 'unit_rent']]

# 按居数给所有df进行分组
beijing_room_dict = dict(list(beijing_room.groupby('room')))
shanghai_room_dict = dict(list(shanghai_room.groupby('room')))
guangzhou_room_dict = dict(list(guangzhou_room.groupby('room')))
shenzhen_room_dict = dict(list(shenzhen_room.groupby('room')))
quanzhou_room_dict = dict(list(quanzhou_room.groupby('room')))

# 计算所有城市的最小值、最大值、均价和中位数
room1_low, room1_high, room1_mean, room1_mid = get_stat(1)
room2_low, room2_high, room2_mean, room2_mid = get_stat(2)
room3_low, room3_high, room3_mean, room3_mid = get_stat(3)

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
city = ['北京', '上海', '广州', '深圳', '泉州']     # x刻度标签
room = ['一居', '二居', '三居']                   # legend标签
x = np.array([1, 2, 3, 4, 5])                   # x坐标
# 画图
plot_graph(1, room1_low[0], room2_low[0], room3_low[0])
plot_graph(2, room1_high[0], room2_high[0], room3_high[0])
plot_graph(3, room1_mean[0], room2_mean[0], room3_mean[0])
plot_graph(4, room1_mid[0], room2_mid[0], room3_mid[0])
plot_graph(5, room1_low[1], room2_low[1], room3_low[1])
plot_graph(6, room1_high[1], room2_high[1], room3_high[1])
plot_graph(7, room1_mean[1], room2_mean[1], room3_mean[1])
plot_graph(8, room1_mid[1], room2_mid[1], room3_mid[1])
