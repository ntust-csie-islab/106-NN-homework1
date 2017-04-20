import numpy as np
import sys
import os
import subprocess
from sklearn import linear_model
from sklearn.isotonic import IsotonicRegression

##############
listmape=list()
dictmape=dict()


dicttrain=dict()
dicttrain['all']=list()   # for static all data

filepath_train=sys.argv[1]
f = open(filepath_train)
for line in f.readlines()[1:]:
  listline=line.strip().split(',')
  tag=listline[0]+','+listline[1]

  #load traindata 
  listline2=list()
  for item in listline[2:]:
    #print 'item:',item
    #print 'float:',float(item)
    #print 'round:',round(float(item),3)
    listline2.append(round(float(item),4))

  #traindata save to dict by tag
  if dicttrain.get(tag) != None:
    dicttrain[tag].append(listline2)
    dicttrain['all'].append(listline2)
  else: 
    dicttrain[tag]=list()
    dicttrain[tag].append(listline2)

#for key,value in dicttrain.items():
#   print key, value

"""
#static data
ndarraytrainall = np.array(dicttrain['all'])
targetall=ndarraytrainall[0:,0]
hist, bins = np.histogram(targetall, bins=10)
print hist
print bins
"""

print 'intersection_id,tollgate_id,time_window,avg_travel_time'

filepath=sys.argv[2]
f = open(filepath)
for line in f.readlines()[1:]:
  listline=line.strip().split(',')

  #select model
  tag=listline[0]+','+listline[1]
  
  #############################################

  #load traindata to np format
  if dicttrain.get(tag) == None:
    continue

  #if tag!='C;3;"[2016-10-22 08:20:00,2016-10-22 08:40:00)"': 
  #  continue

  #print dicttrain[tag]
  ndarraytrain = np.array(dicttrain[tag])
  target=ndarraytrain[0:-1,0]
  data_train=ndarraytrain[0:-1,1:3]
  #print 'target,data_train:',target,data_train

  #training
  regr = linear_model.LinearRegression()
  #regr = linear_model.BayesianRidge()
  #regr = linear_model.SGDRegressor()
  #regr = IsotonicRegression()
  #regr = linear_model.Ridge(alpha=3)
  #regr = linear_model.Ridge(alpha=0.1)
  #regr = linear_model.Lasso(alpha=0.1)
  #regr = linear_model.Lasso(alpha=1)
  #regr = linear_model.LassoLars(alpha=0.9)
  #regr = linear_model.LassoLars(alpha=0.1)
 
   
  regr.fit(data_train,target)
  #regr.fit_transform(data_train, target)

  ###evaluate traindata
  target_e=ndarraytrain[-1,0]
  data_train_e=[ndarraytrain[-1,1:3]]
  #print np.round(target_e,2),np.round(data_train_e,2)
  #data_train = data_train[-1:]
  #target_e = target[-1:]


  result=regr.predict(data_train_e)

  if result>np.amax(target) or result<np.amin(target):result=np.average(target)

  mape=round(np.mean(np.abs((target_e -result) / target_e)),5)
  listmape.append(mape)
  dictmape[mape]=tag

  #for debug
  #print tag,mape,np.round(target-result,2)
  #print tag,mape,np.round(target,2)
  print tag,mape,np.round(target,2),round(target_e,2),'predict:',round(result,2)
  #print tag,mape

  """
  #for debug more detail 
  np.set_printoptions(suppress=True)
  print 'traindata:'
  for f,t in zip(data_train,target):
    print f,t
  print 'evaluation:'
  print data_train_e,target_e
  """

  """
  ##############################################
  #load testdata to np format 
  listline2=list()
  for item in listline[2:]:
    listline2.append(float(item))
  ndarraytest = np.array([listline2])
  #print ndarraytest

  #testing 
  result=regr.predict(ndarraytest)
  if result>np.amax(target) or result<np.amin(target):result=np.average(target)

  #output 
  print tag.replace(';',',')+','+str(round(result,2))
  """

ndarraymape = np.array(listmape)
print np.average(ndarraymape)
print 'max is',np.amax(ndarraymape)
print dictmape[np.amax(ndarraymape)]
