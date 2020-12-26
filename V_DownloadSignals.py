import webbrowser
import pyautogui
import pandas as pd
import datetime
import os
import time

fileName1 = 'e:\\downloads\\vistalytics_balanced'
fileName = fileName1 + '.csv'

# Remove if exists. We will download and use the latest file.
try:
    os.remove(fileName)
except OSError as e:
    pass
#    print("Error: %s : %s" % (fileName, e.strerror))

# Download signal file
webbrowser.open("http://beta.kosha.vistalytics.com/systemWatchlistTiming?type=vistalytics_balanced&username=chanchal.mahra@gmail.com", new=1)
pyautogui.moveTo(1599,1137,10)
pyautogui.click()
pyautogui.write('1224Bryan!!')
pyautogui.moveTo(1927,1316,1)
pyautogui.click()


time.sleep(3)

df = pd.read_csv(fileName, header=1)
df = df[df['Change'] == 'Yes'] # only read the changed records

tradeDay2 = df.columns[1]
tradeDay1 = df.columns[2]

# save file with date suffix
datetime_obj = datetime.datetime.strptime(tradeDay1, '%Y/%m/%d')
filename2 = 'C:\\Users\\CXM\\Desktop\\Vistalytics\\vistalytics_balanced' + '_' + str((datetime_obj.date())) + '.csv'
df.to_csv(filename2, index=False)

# Create daily candidates file
sell = 'SELL'
buy = 'BUY'

date_col = []
symbol_col = []
signal_col = []
final = {'Date': 0, 'Symbol': symbol_col, 'Signal': signal_col}

for index, row in df.iterrows():
    final['Date'] = date_col.append(tradeDay1)
    final['Symbol'] = symbol_col.append(row['Asset'].upper())
    if row[tradeDay2] == 'Long' and row[tradeDay1] == 'Neutral':
        final['Signal'] = signal_col.append(sell)
    if row[tradeDay2] == 'Short' and row[tradeDay1] == 'Neutral':
        final['Signal'] = signal_col.append(buy)
    if row[tradeDay2] == 'Neutral' and row[tradeDay1] == 'Long':
        final['Signal'] = signal_col.append(buy)
    if row[tradeDay2] == 'Neutral' and row[tradeDay1] == 'Short':
        final['Signal'] = signal_col.append(sell)
    if row[tradeDay2] == 'Long' and row[tradeDay1] == 'Short':
        final['Signal'] = signal_col.append(sell)
        final['Date'] = date_col.append(tradeDay1)
        final['Symbol'] = symbol_col.append(row['Asset'].upper())
        final['Signal'] = signal_col.append(sell)
    if row[tradeDay2] == 'Short' and row[tradeDay1] == 'Long':
        final['Signal'] = signal_col.append(buy)
        final['Date'] = date_col.append(tradeDay1)
        final['Symbol'] = symbol_col.append(row['Asset'].upper())
        final['Signal'] = signal_col.append(buy)

final['Date'] = date_col
final['Symbol'] = symbol_col
final['Signal'] = signal_col
result = pd.DataFrame.from_dict(final)

result.to_csv('C:\\Users\\CXM\\Desktop\\Vistalytics\\VBalSignals.csv',index=False)