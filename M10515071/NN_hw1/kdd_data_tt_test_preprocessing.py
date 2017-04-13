# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:20:34 2017

@author: raymondluchu
"""

import csv
import numpy as np
import pylab as pl
from copy import deepcopy



#%%-----------import table4_routes----------------------------------------------#
route_list = []
f = open('routes (table 4).csv', 'r')
for route in csv.reader(f):
    route_list.append(route)
route_list.pop(0)

route_dict = {}
for r in route_list:
    route_dict[str(r[0] + r[1])] = r[2].split(',')

f.close()

#%%-------import table3_link and do DataReduction-------------------------------#
link_detail = []
f = open('links (table 3).csv', 'r')
for row in csv.reader(f):
    link_detail.append(row)
f.close()

#'link_id', 'length', 'width', 'lanes', 'in_top', 'out_top', 'lane_width
link_detail.pop(0)

#'link_id', 'length', 'lanes', 'in_top', 'out_top'
for link_info in link_detail:
    link_info.pop(6)
    link_info.pop(2)



#%%---------import table5_all_trajectories--------------------------------------#
traj = []
f = open('trajectories(table 5)_test1.csv', 'r')
for row in csv.reader(f):
    traj.append(row)
f.close()
traj_header = [[]]
traj_header[0] = traj.pop(0)

#%%--------separate complete and incomplete data -------------------------------#
cplt_data = []
incplt_data = []
incplt_data_loss_link = []
for row in traj:
    loss_link = []
    for link in route_dict[row[0]+row[1]]:
        if link+'#' not in row[4]:#!!!!!!!!!
            loss_link.append(link)
    if len(loss_link) > 0:
        incplt_data.append(row)
        incplt_data_loss_link.append(loss_link)
    else:
         cplt_data.append(row)

#%%------get all tt of link(100~123)--------------------------------------------#
link_dict = {}
for row in cplt_data:
    each_link = row[4].split(';')
    for link_info in each_link:
        if link_info.split('#')[0] not in link_dict.keys():
            link_dict[link_info.split('#')[0]] = [link_info.split('#')[2]]
        else:
            link_dict[link_info.split('#')[0]].append(link_info.split('#')[2])



#%%-----modify 1% abnormal tt to median for each link---------------------------#

for link_id in link_dict.keys():
    modify_amount = len(link_dict[link_id]) // 100
    temp = np.array(np.float32(link_dict[link_id]))
    median = np.median(temp)
    diff = []
    for time in link_dict[link_id]:
        diff.append(abs(float(time)-median))
    diff = np.array(diff)
    while modify_amount > 0:    
        link_dict[link_id][diff.argmax()] = median
        modify_amount -= 1

            
#%%-------use modified data to estimate mean for each link----------------------#

link_mean = {}
for link_id in link_dict.keys():
    link_mean[link_id] = np.mean(np.float32(link_dict[link_id]))


#%%----fill in mean to incomplete data------------------------------------------#
new_incplt_data_idx4 = []
for i in range(len(incplt_data)):
    r_id = incplt_data[i][0]+incplt_data[i][1]   
    link_info = incplt_data[i][4].split(';')
    #find out loss_link and then get idx to insert to link_info
    for loss_link in incplt_data_loss_link[i]:
        loss_idx = route_dict[r_id].index(loss_link)
        insert_string = '#'.join([loss_link, 'NAN(datetime)', '%.2f' % link_mean[loss_link]])
        link_info.insert(loss_idx, insert_string)
    new_incplt_data_idx4.append(';'.join(link_info))


fill_done_incplt_data = deepcopy(incplt_data)
for i in range(len(fill_done_incplt_data)):
    fill_done_incplt_data[i][4] = new_incplt_data_idx4[i]

     
#%%-----combine incplt_data and cplt_data---------------------------------------#
combined_data = deepcopy(cplt_data)
for row in fill_done_incplt_data:
    combined_data.append(row)

#%%---------------------------------------------------------------#

with open('clean_kdd_tt_test_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(traj_header)
    w.writerows(combined_data)
