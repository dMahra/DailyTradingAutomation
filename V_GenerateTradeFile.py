import pandas as pd
firstFile = 'C:\\Users\\CXM\\Desktop\\Vistalytics\\VBalSignals.csv'
secondFile = 'C:\\Users\\CXM\\Desktop\\Vistalytics\\VBal.csv'

df1 = pd.read_csv(firstFile)
df2 = pd.read_csv(secondFile)

dictionary = {}
for index, row in df2.iterrows():
    dictionary[row['Symbol']] = (row['Price'], row['Quantity'])

df3 = df1.copy()
price = []
quantity = []
for i, row in df1.iterrows():
    price.append(dictionary[row['Symbol']][0])
    quantity.append(dictionary[row['Symbol']][1])
df3['Price'] = price
df3['Quantity'] = quantity

result = pd.DataFrame.from_dict(df3)

result.to_csv('C:\\Users\\CXM\\Desktop\\Vistalytics\\VBalTrades.csv',index=False)


