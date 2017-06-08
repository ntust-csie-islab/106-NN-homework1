import numpy as np
import sys
import os
from sklearn import linear_model

##############
filepath=sys.argv[1]
f = open(filepath)
dataset = np.loadtxt(f,delimiter=',',skiprows=1)
target=dataset[:,0]
data_train=dataset[:,1:]

f.seek(0)
listhead=f.readlines()[0].strip().split(',')[1:]


regr = linear_model.LinearRegression()
regr.fit(data_train,target)


##evaluate train data

#from sklearn.cross_validation import train_test_split
#train_data,test_data,train_target,test_target = train_test_split(data_train,target, test_size=0.2, random_state=0)

test_data = data_train[-10:]
test_target = target[-10:]
#test_data = data_train
#test_target = target

result=regr.predict(test_data)

#for p,t in zip(result,test_target):
#   print p, t , abs(p-t)

#print np.mean((result-test_target)**2)
print np.mean(np.abs((test_target - result) / test_target))



"""
### predict 

####
filepath=sys.argv[2]
f = open(filepath)
dataset2 = np.loadtxt(f,delimiter=',',skiprows=1)
target2=dataset2[:,0]
data_test=dataset2[:,1:]

listpredict=list()
result=regr.predict(data_test)


###
i=0
f=open('testuniqid')
print 'intersection_id,tollgate_id,time_window,avg_travel_time'
for line in f :
  tmp=line.split(';')
  print tmp[0]+','+tmp[1]+','+tmp[2].strip()+','+str(round(result[i],2))
  i=i+1

"""
