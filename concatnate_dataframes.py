import pandas as pd

for i in range(0,167):
    vars()['df{}'.format(i)] = pd.read_csv('ticker_data_data_'+str(i)+'.csv', index_col=0)

df = []
for i in range(0,167):
    df.append(vars()['df{}'.format(i)])

df_res = pd.concat(df)
df_res.reset_index(inplace = True)
df_res.drop(['index'], axis = 1, inplace = True)
# print(df_res)

df_res.to_csv('ticker_data.csv')

