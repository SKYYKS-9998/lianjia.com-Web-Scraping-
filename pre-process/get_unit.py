import pandas as pd

col = ['rent', 'block', 'area', 'direction', 'room']
beijing_df = pd.read_csv("source_data\\beijing.csv", header=None, names=col)
shanghai_df = pd.read_csv("source_data\\shanghai.csv", header=None, names=col)
guangzhou_df = pd.read_csv("source_data\\guangzhou.csv", header=None, names=col)
shenzhen_df = pd.read_csv("source_data\\shenzhen.csv", header=None, names=col)
quanzhou_df = pd.read_csv("source_data\\quanzhou.csv", header=None, names=col)

# 插入一行，为单位面积租金，取小数点后两位
beijing_df.insert(loc=len(beijing_df.columns), column='unit_rent', value=0)
for index in beijing_df.index:
    beijing_df.loc[index, 'unit_rent'] = round(beijing_df.loc[index, 'rent'] / beijing_df.loc[index, 'area'], 2)

shanghai_df.insert(loc=len(shanghai_df.columns), column='unit_rent', value=0)
for index in shanghai_df.index:
    shanghai_df.loc[index, 'unit_rent'] = round(shanghai_df.loc[index, 'rent'] / shanghai_df.loc[index, 'area'], 2)

guangzhou_df.insert(loc=len(guangzhou_df.columns), column='unit_rent', value=0)
for index in guangzhou_df.index:
    guangzhou_df.loc[index, 'unit_rent'] = round(guangzhou_df.loc[index, 'rent'] / guangzhou_df.loc[index, 'area'], 2)

shenzhen_df.insert(loc=len(shenzhen_df.columns), column='unit_rent', value=0)
for index in shenzhen_df.index:
    shenzhen_df.loc[index, 'unit_rent'] = round(shenzhen_df.loc[index, 'rent'] / shenzhen_df.loc[index, 'area'], 2)

quanzhou_df.insert(loc=len(quanzhou_df.columns), column='unit_rent', value=0)
for index in quanzhou_df.index:
    quanzhou_df.loc[index, 'unit_rent'] = round(quanzhou_df.loc[index, 'rent'] / quanzhou_df.loc[index, 'area'], 2)

beijing_df.to_csv("data_with_unit\\beijing.csv", index=False)
shanghai_df.to_csv("data_with_unit\\shanghai.csv", index=False)
guangzhou_df.to_csv("data_with_unit\\guangzhou.csv", index=False)
shenzhen_df.to_csv("data_with_unit\\shenzhen.csv", index=False)
quanzhou_df.to_csv("data_with_unit\\quanzhou.csv", index=False)

