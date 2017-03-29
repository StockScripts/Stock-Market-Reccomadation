import csv

symbol_list=[]
date_list=[]
prev_close_list=[]
open_price_list=[]
high_price_list=[]
low_price_list=[]
last_price_list=[]
average_price_list=[]
total_traded_quantity_list=[]
close_price_list=[]

with open('Stock_csv/clean-22-01-2016-TO-20-01-2017TCSALLN.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        symbol_list.append(row['Symbol'])
        date_list.append(row['Date'])
        prev_close_list.append(float(row['Prev Close']))
        open_price_list.append(float(row['Open Price']))
        high_price_list.append(float(row['High Price']))
        low_price_list.append(float(row['Low Price']))
        last_price_list.append(float(row['Last Price']))
        average_price_list.append(float(row['Average Price']))
        total_traded_quantity_list.append(int(row['Total Traded Quantity']))
        close_price_list.append(float(row['Close Price']))

close_list=[prev_close_list,close_price_list]

print (len(prev_close_list))

print close_list

volatility_list=[]

for i in range(9,len(prev_close_list)):
    result=0
    for j in range(i-10+1,i):
        result=result+(close_list[0][j]-close_list[1][j])/close_list[1][j]
    volatility=result/10
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

for i in range(9,len(flag_list)):
    result=0
    for j in range(i-10+1,i):
        result=result+flag_list[j]
    momentum_list.append(result/10)
print momentum_list
print (len(momentum_list))


day1=[]
day2=[]
day3=[]
day4=[]
day5=[]

print ('check ::: ',len(close_price_list))

for i in range(0,len(close_price_list)-5):

    count = 0

    result=close_price_list[count+i+1]-close_price_list[i]
    if result >= -1 and result <= 1:
        day1.append(0)
    if result > 1:
        day1.append(1)
    if result < -1:
        day1.append(-1)
    count=count+1

    result = close_price_list[count + i + 1] - close_price_list[i]
    if result >= -1 and result <= 1:
        day2.append(0)
    if result > 1:
        day2.append(1)
    if result < -1:
        day2.append(-1)
    count=count+1

    result = close_price_list[count + i + 1] - close_price_list[i]
    if result >= -1 and result <= 1:
        day3.append(0)
    if result > 1:
        day3.append(1)
    if result < -1:
        day3.append(-1)
    count=count+1

    result = close_price_list[count + i + 1] - close_price_list[i]
    if result >= -1 and result <= 1:
        day4.append(0)
    if result > 1:
        day4.append(1)
    if result < -1:
        day4.append(-1)
    count=count+1

    result = close_price_list[count + i + 1] - close_price_list[i]
    if result >= -1 and result <= 1:
        day5.append(0)
    if result > 1:
        day5.append(1)
    if result < -1:
        day5.append(-1)
    count=count+1

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
for i in range(9,len(percent_change_list)):
    result=0
    for j in range(i-10+1,i):
        result=result+percent_change_list[j]
    volatility_index=result/10
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

for i in range(9,len(flag_list_index)):
    result=0
    for j in range(i-10+1,i):
        result=result+flag_list_index[j]
    momentum_list_index.append(result/10)
print momentum_list_index
print (len(momentum_list_index))

del symbol_list[:9]
del date_list[:9]
del prev_close_list[:9]
del open_price_list[:9]
del high_price_list[:9]
del low_price_list[:9]
del last_price_list[:9]
del average_price_list[:9]
del total_traded_quantity_list[:9]
del close_price_list[:9]

del day1[:9]
del day2[:9]
del day3[:9]
del day4[:9]
del day5[:9]

print ('check ::: ',len(day1))
print ('check ::: ',len(day2))
print ('check ::: ',len(day3))
print ('check ::: ',len(day4))
print ('check ::: ',len(day5))

with open('Features_stock/features_10day_csv.csv', 'wb') as csvfileWrite:
    fieldnames = ['Id', 'Symbol', 'Date', 'Prev Close', 'Open Price', 'High Price', 'Low Price', 'Lsat Price',
                  'Average Price', 'Total_Traded_Quantity', 'Close Price', 'Momentum of Close Price',
                  'Volatility of Close Price', 'Momentum Bases on Index', 'Volatility Bases on Index','Day1','Day2','Day3','Day4','Day5']
    writer = csv.DictWriter(csvfileWrite, fieldnames=fieldnames)
    writer.writeheader()
    count=0
    for i in range(0, len(day1)):
        writer.writerow(
            {
                'Id': count,
                'Symbol': symbol_list[i],
                'Date': date_list[i],
                'Prev Close': prev_close_list[i],
                'Open Price': open_price_list[i],
                'High Price': high_price_list[i],
                'Low Price': low_price_list[i],
                'Lsat Price': last_price_list[i],
                'Average Price': average_price_list[i],
                'Total_Traded_Quantity': total_traded_quantity_list[i],
                'Close Price': prev_close_list[i],
                'Momentum of Close Price': momentum_list[i],
                'Volatility of Close Price': volatility_list[i],
                'Momentum Bases on Index': momentum_list_index[i],
                'Volatility Bases on Index': volatility_index_list[i],
                'Day1':day1[i],
                'Day2':day2[i],
                'Day3':day3[i],
                'Day4':day4[i],
                'Day5':day5[i]
            }
        )
        count=count+1
