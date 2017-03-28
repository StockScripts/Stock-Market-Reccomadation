import csv

symbol_list=[]
date_list=[]
prev_close_list=[]
close_price_list=[]

with open('Stock_csv/clean-22-01-2016-TO-20-01-2017TCSALLN.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        symbol_list.append(row['Symbol'])
        date_list.append(row['Date'])
        prev_close_list.append(float(row['Prev Close']))
        close_price_list.append(float(row['Close Price']))

close_list=[prev_close_list,close_price_list]

print (len(prev_close_list))

print close_list

volatility_list=[]

for i in range(29,len(prev_close_list)):
    result=0
    for j in range(i-30+1,i):
        result=result+(close_list[0][j]-close_list[1][j])/close_list[1][j]
    volatility=result/30
    volatility_list.append(volatility)
print volatility_list
print (len(volatility_list))

flag_list=[]
for k in range(0,len(prev_close_list)):
    temp=close_list[1][k]-close_list[0][k]
    if(temp<0):
        flag_list.append(-1)
    else:
        flag_list.append(1)
print flag_list
print (len(flag_list))


momentum_list=[]

for i in range(29,len(flag_list)):
    result=0
    for j in range(i-30+1,i):
        result=result+flag_list[j]
    momentum_list.append(result/30)
print momentum_list
print (len(momentum_list))


date_list_index=[]
close_list=[]
open_list=[]
percent_change_list=[]

with open('Stock_csv/data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date_list_index.append(row['Date'])
        close_list.append(float(row['Close']))
        open_list.append(float(row['Open']))

print close_list
print open_list
result=0
for i in range(0,len(open_list)):
    open_price=open_list[i]
    close_price=close_list[i]
    if open_price==0:
        result=-100.00
    else:
        if open_price == close_price:
            result = 100.00
        else:
            result = (abs(close_price - open_price) / open_price) * 100;
    percent_change_list.append(result)
print percent_change_list

volatility_index_list=[]
for i in range(29,len(percent_change_list)):
    result=0
    for j in range(i-30+1,i):
        result=result+percent_change_list[j]
    volatility_index=result/30
    volatility_index_list.append(volatility_index)
print volatility_index_list
print (len(volatility_index_list))

volatility_index_list=[]
for i in range(29,len(percent_change_list)):
    result=0
    for j in range(i-30+1,i):
        result=result+percent_change_list[j]
    volatility_index=result/30
    volatility_index_list.append(volatility_index)
print volatility_index_list
print (len(volatility_index_list))

flag_list_index=[]
for k in range(0,len(open_list)):
    temp=close_list[k]-open_list[k]
    if(temp<0):
        flag_list_index.append(-1)
    else:
        flag_list_index.append(1)
print flag_list_index
print (len(flag_list_index))


momentum_list_index=[]

for i in range(29,len(flag_list_index)):
    result=0
    for j in range(i-30+1,i):
        result=result+flag_list_index[j]
    momentum_list_index.append(result/30)
print momentum_list_index
print (len(momentum_list_index))

del close_price_list[:29]
del prev_close_list[:29]
del date_list[:29]
del symbol_list[:29]

with open('Features_stock/features_30day_csv.csv', 'a') as csvfileWrite:
    fieldnames = ['Id','Symbol','Date','Prev Close','Close Price','Momentum of Close Price','Volatility of Close Price','Momentum Bases on Index','Volatility Bases on Index']
    writer = csv.DictWriter(csvfileWrite, fieldnames=fieldnames)
    count=0
    for i in range(0, len(prev_close_list)):
        writer.writerow(
            {
                'Id': count,
                'Symbol': symbol_list[i],
                'Date': date_list[i],
                'Prev Close': prev_close_list[i],
                'Close Price': close_price_list[i],
                'Momentum of Close Price': momentum_list[i],
                'Volatility of Close Price' :volatility_list[i],
                'Momentum Bases on Index': momentum_list_index[i],
                'Volatility Bases on Index' :volatility_index_list[i]
            }
        )
        count=count+1