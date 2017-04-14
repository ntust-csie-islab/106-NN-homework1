import numpy as np
import sys
import os
import subprocess

##############




listavgtime=list()

filepath_train=sys.argv[1]
f = open(filepath_train)
for line in f.readlines()[1:]:
  listline=line.strip().split(',')
  avgtime=float(listline[5].replace('"',''))
  if avgtime<600:  
    listavgtime.append(avgtime)


ndarrayavgtime= np.array(listavgtime)
hist, bins = np.histogram(ndarrayavgtime, bins=10)
print hist
print bins

