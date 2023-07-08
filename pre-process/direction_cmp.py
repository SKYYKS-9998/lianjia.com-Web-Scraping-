import pandas as pd

beijing_df = pd.read_csv("data_with_unit\\beijing.csv")
shanghai_df = pd.read_csv("data_with_unit\\shanghai.csv")
guangzhou_df = pd.read_csv("data_with_unit\\guangzhou.csv")
shenzhen_df = pd.read_csv("data_with_unit\\shenzhen.csv")
quanzhou_df = pd.read_csv("data_with_unit\\quanzhou.csv")

# 只需要朝向和单位面积租金的数据
beijing_direction = beijing_df[['direction', 'unit_rent']]
shanghai_direction = shanghai_df[['direction', 'unit_rent']]
guangzhou_direction = guangzhou_df[['direction', 'unit_rent']]
shenzhen_direction = shenzhen_df[['direction', 'unit_rent']]
quanzhou_direction = quanzhou_df[['direction', 'unit_rent']]

# 一条数据可能有多个朝向，改为多条只有一个朝向的数据
beijing_direction_new = pd.DataFrame(columns=['direction', 'unit_rent'])
for index, row in beijing_direction.iterrows():
    dir_list = row['direction'].split()
    for i in range(len(dir_list)):
        row['direction'] = dir_list[i]
        beijing_direction_new = beijing_direction_new.append(row)
shanghai_direction_new = pd.DataFrame(columns=['direction', 'unit_rent'])
for index, row in shanghai_direction.iterrows():
    dir_list = row['direction'].split()
    for i in range(len(dir_list)):
        row['direction'] = dir_list[i]
        shanghai_direction_new = shanghai_direction_new.append(row)
guangzhou_direction_new = pd.DataFrame(columns=['direction', 'unit_rent'])
for index, row in guangzhou_direction.iterrows():
    dir_list = row['direction'].split()
    for i in range(len(dir_list)):
        row['direction'] = dir_list[i]
        guangzhou_direction_new = guangzhou_direction_new.append(row)
shenzhen_direction_new = pd.DataFrame(columns=['direction', 'unit_rent'])
for index, row in shenzhen_direction.iterrows():
    dir_list = row['direction'].split()
    for i in range(len(dir_list)):
        row['direction'] = dir_list[i]
        shenzhen_direction_new = shenzhen_direction_new.append(row)
quanzhou_direction_new = pd.DataFrame(columns=['direction', 'unit_rent'])
for index, row in quanzhou_direction.iterrows():
    dir_list = row['direction'].split()
    for i in range(len(dir_list)):
        row['direction'] = dir_list[i]
        quanzhou_direction_new = quanzhou_direction_new.append(row)

# 按朝向进行分组
beijing_direction_dict = dict(list(beijing_direction_new.groupby('direction')))
shanghai_direction_dict = dict(list(shanghai_direction_new.groupby('direction')))
guangzhou_direction_dict = dict(list(guangzhou_direction_new.groupby('direction')))
shenzhen_direction_dict = dict(list(shenzhen_direction_new.groupby('direction')))
quanzhou_direction_dict = dict(list(quanzhou_direction_new.groupby('direction')))

# 计算每个朝向的单位面积租金均价
beijing_direction_mean = {}
for key in beijing_direction_dict.keys():
    beijing_direction_mean[key] = round(beijing_direction_dict[key]['unit_rent'].mean(), 2)
shanghai_direction_mean = {}
for key in shanghai_direction_dict.keys():
    shanghai_direction_mean[key] = round(shanghai_direction_dict[key]['unit_rent'].mean(), 2)
guangzhou_direction_mean = {}
for key in guangzhou_direction_dict.keys():
    guangzhou_direction_mean[key] = round(guangzhou_direction_dict[key]['unit_rent'].mean(), 2)
shenzhen_direction_mean = {}
for key in shenzhen_direction_dict.keys():
    shenzhen_direction_mean[key] = round(shenzhen_direction_dict[key]['unit_rent'].mean(), 2)
quanzhou_direction_mean = {}
for key in quanzhou_direction_dict.keys():
    quanzhou_direction_mean[key] = round(quanzhou_direction_dict[key]['unit_rent'].mean(), 2)

# 按单位面积租金均价从小到大排序
beijing_direction_mean = dict(sorted(beijing_direction_mean.items(), key=lambda item: item[1]))
shanghai_direction_mean = dict(sorted(shanghai_direction_mean.items(), key=lambda item: item[1]))
guangzhou_direction_mean = dict(sorted(guangzhou_direction_mean.items(), key=lambda item: item[1]))
shenzhen_direction_mean = dict(sorted(shenzhen_direction_mean.items(), key=lambda item: item[1]))
quanzhou_direction_mean = dict(sorted(quanzhou_direction_mean.items(), key=lambda item: item[1]))

# 将五个城市的朝向和单位面积均价合并到一个df，然后输出csv
beijing_data = {'朝向(北京)': beijing_direction_mean.keys(), '租金均价(元)(北京)': beijing_direction_mean.values()}
beijing_result_df = pd.DataFrame(beijing_data)
shanghai_data = {'朝向(上海)': shanghai_direction_mean.keys(), '租金均价(元)(上海)': shanghai_direction_mean.values()}
shanghai_result_df = pd.DataFrame(shanghai_data)
guangzhou_data = {'朝向(广州)': guangzhou_direction_mean.keys(), '租金均价(元)(广州)': guangzhou_direction_mean.values()}
guangzhou_result_df = pd.DataFrame(guangzhou_data)
shenzhen_data = {'朝向(深圳)': shenzhen_direction_mean.keys(), '租金均价(元)(深圳)': shenzhen_direction_mean.values()}
shenzhen_result_df = pd.DataFrame(shenzhen_data)
quanzhou_data = {'朝向(泉州)': quanzhou_direction_mean.keys(), '租金均价(元)(泉州)': quanzhou_direction_mean.values()}
quanzhou_result_df = pd.DataFrame(quanzhou_data)
total_df = pd.concat([beijing_result_df, shanghai_result_df, guangzhou_result_df,
                      shenzhen_result_df, quanzhou_result_df], axis=1)
total_df.to_csv('fig_q5\\五个城市每种朝向租金均价.csv', index=False)
