import pandas as pd

beijing_df = pd.read_csv("data_with_unit\\beijing.csv")
shanghai_df = pd.read_csv("data_with_unit\\shanghai.csv")
guangzhou_df = pd.read_csv("data_with_unit\\guangzhou.csv")
shenzhen_df = pd.read_csv("data_with_unit\\shenzhen.csv")
quanzhou_df = pd.read_csv("data_with_unit\\quanzhou.csv")

# 只需要板块和租金的数据
beijing_block = beijing_df[['block', 'rent']]
shanghai_block = shanghai_df[['block', 'rent']]
guangzhou_block = guangzhou_df[['block', 'rent']]
shenzhen_block = shenzhen_df[['block', 'rent']]
quanzhou_block = quanzhou_df[['block', 'rent']]

# 按板块分组
beijing_block_dict = dict(list(beijing_block.groupby('block')))
shanghai_block_dict = dict(list(shanghai_block.groupby('block')))
guangzhou_block_dict = dict(list(guangzhou_block.groupby('block')))
shenzhen_block_dict = dict(list(shenzhen_block.groupby('block')))
quanzhou_block_dict = dict(list(quanzhou_block.groupby('block')))

# 计算每个板块的租金均价，存在dict里
beijing_block_mean = {}
for key in beijing_block_dict.keys():
    beijing_block_mean[key] = round(beijing_block_dict[key]['rent'].mean(), 2)
shanghai_block_mean = {}
for key in shanghai_block_dict.keys():
    shanghai_block_mean[key] = round(shanghai_block_dict[key]['rent'].mean(), 2)
guangzhou_block_mean = {}
for key in guangzhou_block_dict.keys():
    guangzhou_block_mean[key] = round(guangzhou_block_dict[key]['rent'].mean(), 2)
shenzhen_block_mean = {}
for key in shenzhen_block_dict.keys():
    shenzhen_block_mean[key] = round(shenzhen_block_dict[key]['rent'].mean(), 2)
quanzhou_block_mean = {}
for key in quanzhou_block_dict.keys():
    quanzhou_block_mean[key] = round(quanzhou_block_dict[key]['rent'].mean(), 2)

# 按租金均价从大到小排序
beijing_block_mean = dict(sorted(beijing_block_mean.items(), key=lambda item: item[1], reverse=True))
shanghai_block_mean = dict(sorted(shanghai_block_mean.items(), key=lambda item: item[1], reverse=True))
guangzhou_block_mean = dict(sorted(guangzhou_block_mean.items(), key=lambda item: item[1], reverse=True))
shenzhen_block_mean = dict(sorted(shenzhen_block_mean.items(), key=lambda item: item[1], reverse=True))
quanzhou_block_mean = dict(sorted(quanzhou_block_mean.items(), key=lambda item: item[1], reverse=True))

# 输出csv文件
beijing_data = {'板块': beijing_block_mean.keys(), '租金均价(元)': beijing_block_mean.values()}
beijing_result_df = pd.DataFrame(beijing_data)
beijing_result_df.to_csv('fig_q4\\北京每个板块租金均价.csv', index=False)
shanghai_data = {'板块': shanghai_block_mean.keys(), '租金均价(元)': shanghai_block_mean.values()}
shanghai_result_df = pd.DataFrame(shanghai_data)
shanghai_result_df.to_csv('fig_q4\\上海每个板块租金均价.csv', index=False)
guangzhou_data = {'板块': guangzhou_block_mean.keys(), '租金均价(元)': guangzhou_block_mean.values()}
guangzhou_result_df = pd.DataFrame(guangzhou_data)
guangzhou_result_df.to_csv('fig_q4\\广州每个板块租金均价.csv', index=False)
shenzhen_data = {'板块': shenzhen_block_mean.keys(), '租金均价(元)': shenzhen_block_mean.values()}
shenzhen_result_df = pd.DataFrame(shenzhen_data)
shenzhen_result_df.to_csv('fig_q4\\深圳每个板块租金均价.csv', index=False)
quanzhou_data = {'板块': quanzhou_block_mean.keys(), '租金均价(元)': quanzhou_block_mean.values()}
quanzhou_result_df = pd.DataFrame(quanzhou_data)
quanzhou_result_df.to_csv('fig_q4\\泉州每个板块租金均价.csv', index=False)
