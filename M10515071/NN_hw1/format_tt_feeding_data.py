# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:01:03 2017

@author: raymondluchu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:32:58 2017

@author: raymondluchu
"""



import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import datetime


#%%----get all clean_tt_data----------------------------------------------------#
tt_data = []
with open('clean_kdd_tt_data.csv', 'r') as f:
    for row in csv.reader(f):
        tt_data.append(row)
        
tt_header = tt_data.pop(0)

#%%-----remove unnecessary field and add datetime-----------------------------#
for row in tt_data:
    del row[4]
    del row[2]
    t_struct = time.strptime(row[2],'%Y-%m-%d %H:%M:%S')
    t_mon = t_struct[1]
    t_day = t_struct[2]
    t_h = t_struct[3]
    t_m = t_struct[4]//20 * 20 + 10
    t_wday = t_struct[6] + 1
    row.append(t_mon)
    row.append(t_day)
    row.append(t_wday)
    row.append(t_h)
    row.append(t_m)
    row.append(datetime.datetime(2016,t_mon,t_day,t_h,t_m))

#%%------six routes x,y data list----------#
a2_x_p1 = []
a2_x_p2 = []
a2_y_p1 = []
a2_y_p2 = []

a3_x_p1 = []
a3_x_p2 = []
a3_y_p1 = []
a3_y_p2 = []

b1_x_p1 = []
b1_x_p2 = []
b1_y_p1 = []
b1_y_p2 = []

b3_x_p1 = []
b3_x_p2 = []
b3_y_p1 = []
b3_y_p2 = []

c1_x_p1 = []
c1_x_p2 = []
c1_y_p1 = []
c1_y_p2 = []

c3_x_p1 = []
c3_x_p2 = []
c3_y_p1 = []
c3_y_p2 = []
#%%------six routes x,y median list----------#
a2_x_p1_median = []
a2_x_p2_median = []
a2_y_p1_median = []
a2_y_p2_median = []

a3_x_p1_median = []
a3_x_p2_median = []
a3_y_p1_median = []
a3_y_p2_median = []

b1_x_p1_median = []
b1_x_p2_median = []
b1_y_p1_median = []
b1_y_p2_median = []

b3_x_p1_median = []
b3_x_p2_median = []
b3_y_p1_median = []
b3_y_p2_median = []

c1_x_p1_median = []
c1_x_p2_median = []
c1_y_p1_median = []
c1_y_p2_median = []

c3_x_p1_median = []
c3_x_p2_median = []
c3_y_p1_median = []
c3_y_p2_median = []
#%%-----separate six_routes to above list------------------#
for row in tt_data:
    if row[0]=='A' and row[1]=='2' and (row[7] in [6,7]):
        a2_x_p1.append(row)
        a2_x_p1_median.append(float(row[3]))
    elif row[0]=='A' and row[1]=='2' and (row[7] in [15,16]):
        a2_x_p2.append(row)
        a2_x_p2_median.append(float(row[3]))
    elif row[0]=='A' and row[1]=='2' and (row[7] in [8,9]):
        a2_y_p1.append(row)
        a2_y_p1_median.append(float(row[3]))
    elif row[0]=='A' and row[1]=='2' and (row[7] in [17,18]):
        a2_y_p2.append(row)
        a2_y_p2_median.append(float(row[3]))
#        
    elif row[0]=='A' and row[1]=='3' and (row[7] in [6,7]):
        a3_x_p1.append(row)
        a3_x_p1_median.append(float(row[3]))
    elif row[0]=='A' and row[1]=='3' and (row[7] in [15,16]):
        a3_x_p2.append(row)
        a3_x_p2_median.append(float(row[3]))
    elif row[0]=='A' and row[1]=='3' and (row[7] in [8,9]):
        a3_y_p1.append(row)
        a3_y_p1_median.append(float(row[3]))
    elif row[0]=='A' and row[1]=='3' and (row[7] in [17,18]):
        a3_y_p2.append(row)
        a3_y_p2_median.append(float(row[3]))
#        
    elif row[0]=='B' and row[1]=='1' and (row[7] in [6,7]):
        b1_x_p1.append(row)
        b1_x_p1_median.append(float(row[3]))
    elif row[0]=='B' and row[1]=='1' and (row[7] in [15,16]):
        b1_x_p2.append(row)
        b1_x_p2_median.append(float(row[3]))
    elif row[0]=='B' and row[1]=='1' and (row[7] in [8,9]):
        b1_y_p1.append(row)
        b1_y_p1_median.append(float(row[3]))
    elif row[0]=='B' and row[1]=='1' and (row[7] in [17,18]):
        b1_y_p2.append(row)
        b1_y_p2_median.append(float(row[3]))
#        
    elif row[0]=='B' and row[1]=='3' and (row[7] in [6,7]):
        b3_x_p1.append(row)
        b3_x_p1_median.append(float(row[3]))
    elif row[0]=='B' and row[1]=='3' and (row[7] in [15,16]):
        b3_x_p2.append(row)
        b3_x_p2_median.append(float(row[3]))
    elif row[0]=='B' and row[1]=='3' and (row[7] in [8,9]):
        b3_y_p1.append(row)
        b3_y_p1_median.append(float(row[3]))
    elif row[0]=='B' and row[1]=='3' and (row[7] in [17,18]):
        b3_y_p2.append(row)
        b3_y_p2_median.append(float(row[3]))
#        
    elif row[0]=='C' and row[1]=='1' and (row[7] in [6,7]):
        c1_x_p1.append(row)
        c1_x_p1_median.append(float(row[3]))
    elif row[0]=='C' and row[1]=='1' and (row[7] in [15,16]):
        c1_x_p2.append(row)
        c1_x_p2_median.append(float(row[3]))
    elif row[0]=='C' and row[1]=='1' and (row[7] in [8,9]):
        c1_y_p1.append(row)
        c1_y_p1_median.append(float(row[3]))
    elif row[0]=='C' and row[1]=='1' and (row[7] in [17,18]):
        c1_y_p2.append(row)
        c1_y_p2_median.append(float(row[3]))
#        
    elif row[0]=='C' and row[1]=='3' and (row[7] in [6,7]):
        c3_x_p1.append(row)
        c3_x_p1_median.append(float(row[3]))
    elif row[0]=='C' and row[1]=='3' and (row[7] in [15,16]):
        c3_x_p2.append(row)
        c3_x_p2_median.append(float(row[3]))
    elif row[0]=='C' and row[1]=='3' and (row[7] in [8,9]):
        c3_y_p1.append(row)
        c3_y_p1_median.append(float(row[3]))
    elif row[0]=='C' and row[1]=='3' and (row[7] in [17,18]):
        c3_y_p2.append(row)
        c3_y_p2_median.append(float(row[3]))

#%%--get median for each interval to fill in some interval that haven't mean----#
a2_x_p1_median.sort()
a2_x_p2_median.sort()
a2_y_p1_median.sort()
a2_y_p2_median.sort()

a3_x_p1_median.sort()
a3_x_p2_median.sort()
a3_y_p1_median.sort()
a3_y_p2_median.sort()

b1_x_p1_median.sort()
b1_x_p2_median.sort()
b1_y_p1_median.sort()
b1_y_p2_median.sort()

b3_x_p1_median.sort()
b3_x_p2_median.sort()
b3_y_p1_median.sort()
b3_y_p2_median.sort()

c1_x_p1_median.sort()
c1_x_p2_median.sort()
c1_y_p1_median.sort()
c1_y_p2_median.sort()

c3_x_p1_median.sort()
c3_x_p2_median.sort()
c3_y_p1_median.sort()
c3_y_p2_median.sort()

#==============================================================================
# all_route = {'a2_x_p1':[] ,'a2_x_p2':[], 'a2_y_p1':[] ,'a2_y_p2':[],
#              'a3_x_p1':[] ,'a3_x_p2':[], 'a3_y_p1':[] ,'a3_y_p2':[],
#              'b1_x_p1':[] ,'b1_x_p2':[], 'b1_y_p1':[] ,'b1_y_p2':[],
#              'b3_x_p1':[] ,'b3_x_p2':[], 'b3_y_p1':[] ,'b3_y_p2':[],
#              'c1_x_p1':[] ,'c1_x_p2':[], 'c1_y_p1':[] ,'c1_y_p2':[],
#              'c3_x_p1':[] ,'c3_x_p2':[], 'c3_y_p1':[] ,'c3_y_p2':[]}
#==============================================================================
#==============================================================================
# temp = []
# for row in a2_x_p1:
#     temp.append(float(row[3]))
# temp.sort()
# if len(temp) % 2 == 0:
#     a2xp1_median = ( temp[len(temp)//2- 1] + temp[len(temp)//2] ) / 2
# else:
#     a2xp1_median = temp[len(temp)//2]  
#==============================================================================
#%%---format A2 x,y_data as [[t1~t6(0719)],[t1~t6(0720)],...,[t1~t6(1017)]]---#

first_day = datetime.datetime(2016,7,19,6,10)
temp = []
a_interval = []
a2_x_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a2_x_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a2_x_p1_median[len(a2_x_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a2_x_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)
#----

first_day = datetime.datetime(2016,7,19,15,10)
temp = []
a_interval = []
a2_x_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a2_x_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a2_x_p2_median[len(a2_x_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a2_x_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)       
#----

first_day = datetime.datetime(2016,7,19,8,10)
temp = []
a_interval = []
a2_y_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a2_y_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a2_y_p1_median[len(a2_y_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a2_y_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)        
#----

first_day = datetime.datetime(2016,7,19,17,10)
temp = []
a_interval = []
a2_y_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a2_y_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a2_y_p2_median[len(a2_y_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a2_y_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)      
#--
#%%---format A3 x,y_data as [[t1~t6(0719)],[t1~t6(0720)],...,[t1~t6(1017)]]---#

first_day = datetime.datetime(2016,7,19,6,10)
temp = []
a_interval = []
a3_x_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a3_x_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a3_x_p1_median[len(a3_x_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a3_x_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)
#----

first_day = datetime.datetime(2016,7,19,15,10)
temp = []
a_interval = []
a3_x_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a3_x_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a3_x_p2_median[len(a3_x_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a3_x_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)       
#----

first_day = datetime.datetime(2016,7,19,8,10)
temp = []
a_interval = []
a3_y_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a3_y_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a3_y_p1_median[len(a3_y_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a3_y_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)        
#----

first_day = datetime.datetime(2016,7,19,17,10)
temp = []
a_interval = []
a3_y_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in a3_y_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = a3_y_p2_median[len(a3_y_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        a3_y_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)      
#--
#%%---format B1 x,y_data as [[t1~t6(0719)],[t1~t6(0720)],...,[t1~t6(1017)]]---#

first_day = datetime.datetime(2016,7,19,6,10)
temp = []
a_interval = []
b1_x_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b1_x_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b1_x_p1_median[len(b1_x_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b1_x_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)
#----

first_day = datetime.datetime(2016,7,19,15,10)
temp = []
a_interval = []
b1_x_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b1_x_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b1_x_p2_median[len(b1_x_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b1_x_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)       
#----

first_day = datetime.datetime(2016,7,19,8,10)
temp = []
a_interval = []
b1_y_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b1_y_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b1_y_p1_median[len(b1_y_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b1_y_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)        
#----

first_day = datetime.datetime(2016,7,19,17,10)
temp = []
a_interval = []
b1_y_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b1_y_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b1_y_p2_median[len(b1_y_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b1_y_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)      
#--
#%%---format B3 x,y_data as [[t1~t6(0719)],[t1~t6(0720)],...,[t1~t6(1017)]]---#

first_day = datetime.datetime(2016,7,19,6,10)
temp = []
a_interval = []
b3_x_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b3_x_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b3_x_p1_median[len(b3_x_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b3_x_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)
#----

first_day = datetime.datetime(2016,7,19,15,10)
temp = []
a_interval = []
b3_x_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b3_x_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b3_x_p2_median[len(b3_x_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b3_x_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)       
#----

first_day = datetime.datetime(2016,7,19,8,10)
temp = []
a_interval = []
b3_y_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b3_y_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b3_y_p1_median[len(b3_y_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b3_y_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)        
#----

first_day = datetime.datetime(2016,7,19,17,10)
temp = []
a_interval = []
b3_y_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in b3_y_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = b3_y_p2_median[len(b3_y_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        b3_y_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)      
#--
#%%---format C1 x,y_data as [[t1~t6(0719)],[t1~t6(0720)],...,[t1~t6(1017)]]---#

first_day = datetime.datetime(2016,7,19,6,10)
temp = []
a_interval = []
c1_x_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c1_x_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c1_x_p1_median[len(c1_x_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c1_x_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)
#----

first_day = datetime.datetime(2016,7,19,15,10)
temp = []
a_interval = []
c1_x_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c1_x_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c1_x_p2_median[len(c1_x_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c1_x_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)       
#----

first_day = datetime.datetime(2016,7,19,8,10)
temp = []
a_interval = []
c1_y_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c1_y_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c1_y_p1_median[len(c1_y_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c1_y_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)        
#----

first_day = datetime.datetime(2016,7,19,17,10)
temp = []
a_interval = []
c1_y_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c1_y_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c1_y_p2_median[len(c1_y_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c1_y_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)      
#--
#%%---format C3 x,y_data as [[t1~t6(0719)],[t1~t6(0720)],...,[t1~t6(1017)]]---#

first_day = datetime.datetime(2016,7,19,6,10)
temp = []
a_interval = []
c3_x_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c3_x_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c3_x_p1_median[len(c3_x_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c3_x_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)
#----

first_day = datetime.datetime(2016,7,19,15,10)
temp = []
a_interval = []
c3_x_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c3_x_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c3_x_p2_median[len(c3_x_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c3_x_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)       
#----

first_day = datetime.datetime(2016,7,19,8,10)
temp = []
a_interval = []
c3_y_p1_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c3_y_p1:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c3_y_p1_median[len(c3_y_p1_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c3_y_p1_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)        
#----

first_day = datetime.datetime(2016,7,19,17,10)
temp = []
a_interval = []
c3_y_p2_each_day = []
for t_20 in range(546):
    temp = []
    #if t_20 % 6 == 0:
        #a_interval.append(first_day.timetuple()[6] + 1)
    for row in c3_y_p2:
        if row[9]==first_day:
            temp.append(float(row[3]))
    if len(temp) > 0:
        mean = sum(temp) / len(temp)
    else:
        mean = c3_y_p2_median[len(c3_y_p2_median)//2]
    
    a_interval.append(float('%.2f'%mean))
    if len(a_interval) % 6 == 0:
        first_day = first_day + datetime.timedelta(days=1,seconds=-6000)
        c3_y_p2_each_day.append(a_interval)
        a_interval = []
    else:
        first_day = first_day + datetime.timedelta(seconds=1200)      
#--
#%%----save to csv--------------#
with open('feeding_tt/a2xp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a2_x_p1_each_day)
with open('feeding_tt/a2xp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a2_x_p2_each_day)
with open('feeding_tt/a2yp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a2_y_p1_each_day)
with open('feeding_tt/a2yp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a2_y_p2_each_day)
#----
with open('feeding_tt/a3xp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a3_x_p1_each_day)
with open('feeding_tt/a3xp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a3_x_p2_each_day)
with open('feeding_tt/a3yp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a3_y_p1_each_day)
with open('feeding_tt/a3yp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(a3_y_p2_each_day)
#--
with open('feeding_tt/b1xp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b1_x_p1_each_day)
with open('feeding_tt/b1xp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b1_x_p2_each_day)
with open('feeding_tt/b1yp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b1_y_p1_each_day)
with open('feeding_tt/b1yp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b1_y_p2_each_day)
#--
with open('feeding_tt/b3xp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b3_x_p1_each_day)
with open('feeding_tt/b3xp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b3_x_p2_each_day)
with open('feeding_tt/b3yp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b3_y_p1_each_day)
with open('feeding_tt/b3yp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(b3_y_p2_each_day)
#--
with open('feeding_tt/c1xp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c1_x_p1_each_day)
with open('feeding_tt/c1xp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c1_x_p2_each_day)
with open('feeding_tt/c1yp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c1_y_p1_each_day)
with open('feeding_tt/c1yp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c1_y_p2_each_day)
#--
with open('feeding_tt/c3xp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c3_x_p1_each_day)
with open('feeding_tt/c3xp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c3_x_p2_each_day)
with open('feeding_tt/c3yp1.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c3_y_p1_each_day)
with open('feeding_tt/c3yp2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(c3_y_p2_each_day)
#--
