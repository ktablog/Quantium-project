import os
import glob
import pandas as pd

path = "D:\SoftwareDevelopment\_FORAGE\Quantium\quantium-project\quantium-starter-repo\data"
csv_files = glob.glob(path + "/*.csv")
df_list = (pd.read_csv(file) for file in csv_files)
df   = pd.concat(df_list, ignore_index=True)
print(df)
df = df[df['product'].str.contains('pink')]
print(df)
df['price'] = df['price'].str.replace('$', '', regex=True)
df['price'] = df['price'].astype(float)
df['quantity'] = df['quantity'].astype(int)
df['sales'] = df['price'] * df['quantity']
print(df)
df.drop('price', inplace=True, axis=1)
df.drop('quantity', inplace=True, axis=1)
df.drop('product', inplace=True, axis=1)
print(df)
df = df.reindex(columns=['sales', 'date', 'region'])
df.to_csv('sales_data.csv')
print(df)
