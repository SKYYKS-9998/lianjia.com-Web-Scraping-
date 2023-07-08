import pandas as pd
import numpy as np


def data_select(df):
    df.drop_duplicates(subset=None, keep='first', inplace=True)
    df['name'] = df['name'].str.strip('\n')
    df['name'] = df['name'].str.strip(' ')
    df['area'] = df['area'].str.strip('\n')
    df['area'] = df['area'].str.strip(' ')
    df['direction'] = df['direction'].str.strip('\n')
    df['direction'] = df['direction'].str.strip(' ')
    df['room'] = df['room'].str.strip('\n')
    df['room'] = df['room'].str.strip(' ')
    df = df.replace('', np.nan).dropna(how='any').reset_index(drop=True)

    df['rent'] = df['rent'].astype(int)
    df['plate'] = df['plate'].astype(str)
    df['area'] = df['area'].str[:-2]
    df['area'] = df['area'].astype(float)
    df['room'] = df['room'].str[0:1]

    df.insert(loc=len(df.columns), column='price', value=0)
    df['price'] = df['rent'] / df['area']
    df['price'] = round(df['price'], 4)

    return df


col = ['name', 'rent', 'plate', 'area', 'direction', 'room']
beijing_df = pd.read_csv("61_data\\beijing.csv", header=None, names=col)
beijing_df = beijing_df.replace('', np.nan).dropna(how='any').reset_index(drop=True)  # 只要条件为空，则删掉该行
shanghai_df = pd.read_csv("61_data\\shanghai.csv", header=None, names=col)
shanghai_df = shanghai_df.replace('', np.nan).dropna(how='any').reset_index(drop=True)  # 只要条件为空，则删掉该行
guangzhou_df = pd.read_csv("61_data\\guangzhou.csv", header=None, names=col)
guangzhou_df = guangzhou_df.replace('', np.nan).dropna(how='any').reset_index(drop=True)  # 只要条件为空，则删掉该行
shenzhen_df = pd.read_csv("61_data\\shenzhen.csv", header=None, names=col)
shenzhen_df = shenzhen_df.replace('', np.nan).dropna(how='any').reset_index(drop=True)  # 只要条件为空，则删掉该行
chengdu_df = pd.read_csv("61_data\\chengdu.csv", header=None, names=col)
chengdu_df = chengdu_df.replace('', np.nan).dropna(how='any').reset_index(drop=True)  # 只要条件为空，则删掉该行

beijing_df.to_csv("61_data\\2beijing.csv", index=False)
shanghai_df.to_csv("61_data\\2shanghai.csv", index=False)
guangzhou_df.to_csv("61_data\\2guangzhou.csv", index=False)
shenzhen_df.to_csv("61_data\\2shenzhen.csv", index=False)
chengdu_df.to_csv("61_data\\2chengdu.csv", index=False)

beijing_df = data_select(beijing_df)
shanghai_df = data_select(shanghai_df)
guangzhou_df = data_select(guangzhou_df)
shenzhen_df = data_select(shenzhen_df)
chengdu_df = data_select(chengdu_df)

beijing_df.to_csv("61_data\\beijing1.csv", index=False)
shanghai_df.to_csv("61_data\\shanghai1.csv", index=False)
guangzhou_df.to_csv("61_data\\guangzhou1.csv", index=False)
shenzhen_df.to_csv("61_data\\shenzhen1.csv", index=False)
chengdu_df.to_csv("61_data\\chengdu1.csv", index=False)


