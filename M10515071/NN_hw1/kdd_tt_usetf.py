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


#%%-----def nn_layer----------------------------------------------------#
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size])
                        , dtype=tf.float32, name='weights')
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1
                        , dtype=tf.float32, name='biases')
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b        
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs

#%%------six routes x,y data list----------#
a2_x_p1_each_day = []
a2_x_p2_each_day = []
a2_y_p1_each_day = []
a2_y_p2_each_day = []

a3_x_p1_each_day = []
a3_x_p2_each_day = []
a3_y_p1_each_day = []
a3_y_p2_each_day = []

b1_x_p1_each_day = []
b1_x_p2_each_day = []
b1_y_p1_each_day = []
b1_y_p2_each_day = []

b3_x_p1_each_day = []
b3_x_p2_each_day = []
b3_y_p1_each_day = []
b3_y_p2_each_day = []

c1_x_p1_each_day = []
c1_x_p2_each_day = []
c1_y_p1_each_day = []
c1_y_p2_each_day = []

c3_x_p1_each_day = []
c3_x_p2_each_day = []
c3_y_p1_each_day = []
c3_y_p2_each_day = []

#%%---test_x_data list----------#
a2_x_p1_test = []
a2_x_p2_test = []

a3_x_p1_test = []
a3_x_p2_test = []

b1_x_p1_test = []
b1_x_p2_test = []

b3_x_p1_test = []
b3_x_p2_test = []

c1_x_p1_test = []
c1_x_p2_test = []

c3_x_p1_test = []
c3_x_p2_test = []
#%%---import test_x_data----------#
with open('tt_test_data/a2xp1.csv', 'r') as f:
    for row in csv.reader(f):
        a2_x_p1_test.append(row)
    for i in range(len(a2_x_p1_test)):
        a2_x_p1_test[i] = list(map(float,a2_x_p1_test[i]))
with open('tt_test_data/a2xp2.csv', 'r') as f:
    for row in csv.reader(f):
        a2_x_p2_test.append(row)
    for i in range(len(a2_x_p2_test)):
        a2_x_p2_test[i] = list(map(float,a2_x_p2_test[i]))
#----
with open('tt_test_data/a3xp1.csv', 'r') as f:
    for row in csv.reader(f):
        a3_x_p1_test.append(row)
    for i in range(len(a3_x_p1_test)):
        a3_x_p1_test[i] = list(map(float,a3_x_p1_test[i]))
with open('tt_test_data/a3xp2.csv', 'r') as f:
    for row in csv.reader(f):
        a3_x_p2_test.append(row)
    for i in range(len(a3_x_p2_test)):
        a3_x_p2_test[i] = list(map(float,a3_x_p2_test[i]))
#--
with open('tt_test_data/b1xp1.csv', 'r') as f:
    for row in csv.reader(f):
        b1_x_p1_test.append(row)
    for i in range(len(b1_x_p1_test)):
        b1_x_p1_test[i] = list(map(float,b1_x_p1_test[i]))
with open('tt_test_data/b1xp2.csv', 'r') as f:
    for row in csv.reader(f):
        b1_x_p2_test.append(row)
    for i in range(len(b1_x_p2_test)):
        b1_x_p2_test[i] = list(map(float,b1_x_p2_test[i]))
#--
with open('tt_test_data/b3xp1.csv', 'r') as f:
    for row in csv.reader(f):
        b3_x_p1_test.append(row)
    for i in range(len(b3_x_p1_test)):
        b3_x_p1_test[i] = list(map(float,b3_x_p1_test[i]))
with open('tt_test_data/b3xp2.csv', 'r') as f:
    for row in csv.reader(f):
        b3_x_p2_test.append(row)
    for i in range(len(b3_x_p2_test)):
        b3_x_p2_test[i] = list(map(float,b3_x_p2_test[i]))
#--
with open('tt_test_data/c1xp1.csv', 'r') as f:
    for row in csv.reader(f):
        c1_x_p1_test.append(row)
    for i in range(len(c1_x_p1_test)):
        c1_x_p1_test[i] = list(map(float,c1_x_p1_test[i]))
with open('tt_test_data/c1xp2.csv', 'r') as f:
    for row in csv.reader(f):
        c1_x_p2_test.append(row)
    for i in range(len(c1_x_p2_test)):
        c1_x_p2_test[i] = list(map(float,c1_x_p2_test[i]))
#--
with open('tt_test_data/c3xp1.csv', 'r') as f:
    for row in csv.reader(f):
        c3_x_p1_test.append(row)
    for i in range(len(c3_x_p1_test)):
        c3_x_p1_test[i] = list(map(float,c3_x_p1_test[i]))
with open('tt_test_data/c3xp2.csv', 'r') as f:
    for row in csv.reader(f):
        c3_x_p2_test.append(row)
    for i in range(len(c3_x_p2_test)):
        c3_x_p2_test[i] = list(map(float,c3_x_p2_test[i]))


#%%---import 6_routes_24_x_y_data
with open('feeding_tt/a2xp1.csv', 'r') as f:
    for row in csv.reader(f):
        a2_x_p1_each_day.append(row)
    for i in range(len(a2_x_p1_each_day)):
        a2_x_p1_each_day[i] = list(map(float,a2_x_p1_each_day[i]))
with open('feeding_tt/a2xp2.csv', 'r') as f:
    for row in csv.reader(f):
        a2_x_p2_each_day.append(row)
    for i in range(len(a2_x_p2_each_day)):
        a2_x_p2_each_day[i] = list(map(float,a2_x_p2_each_day[i]))
with open('feeding_tt/a2yp1.csv', 'r') as f:
    for row in csv.reader(f):
        a2_y_p1_each_day.append(row)
    for i in range(len(a2_y_p1_each_day)):
        a2_y_p1_each_day[i] = list(map(float,a2_y_p1_each_day[i]))
with open('feeding_tt/a2yp2.csv', 'r') as f:
    for row in csv.reader(f):
        a2_y_p2_each_day.append(row)
    for i in range(len(a2_y_p2_each_day)):
        a2_y_p2_each_day[i] = list(map(float,a2_y_p2_each_day[i]))
#----
with open('feeding_tt/a3xp1.csv', 'r') as f:
    for row in csv.reader(f):
        a3_x_p1_each_day.append(row)
    for i in range(len(a3_x_p1_each_day)):
        a3_x_p1_each_day[i] = list(map(float,a3_x_p1_each_day[i]))
with open('feeding_tt/a3xp2.csv', 'r') as f:
    for row in csv.reader(f):
        a3_x_p2_each_day.append(row)
    for i in range(len(a3_x_p2_each_day)):
        a3_x_p2_each_day[i] = list(map(float,a3_x_p2_each_day[i]))
with open('feeding_tt/a3yp1.csv', 'r') as f:
    for row in csv.reader(f):
        a3_y_p1_each_day.append(row)
    for i in range(len(a3_y_p1_each_day)):
        a3_y_p1_each_day[i] = list(map(float,a3_y_p1_each_day[i]))
with open('feeding_tt/a3yp2.csv', 'r') as f:
    for row in csv.reader(f):
        a3_y_p2_each_day.append(row)
    for i in range(len(a3_y_p2_each_day)):
        a3_y_p2_each_day[i] = list(map(float,a3_y_p2_each_day[i]))
#--
with open('feeding_tt/b1xp1.csv', 'r') as f:
    for row in csv.reader(f):
        b1_x_p1_each_day.append(row)
    for i in range(len(b1_x_p1_each_day)):
        b1_x_p1_each_day[i] = list(map(float,b1_x_p1_each_day[i]))
with open('feeding_tt/b1xp2.csv', 'r') as f:
    for row in csv.reader(f):
        b1_x_p2_each_day.append(row)
    for i in range(len(b1_x_p2_each_day)):
        b1_x_p2_each_day[i] = list(map(float,b1_x_p2_each_day[i]))
with open('feeding_tt/b1yp1.csv', 'r') as f:
    for row in csv.reader(f):
        b1_y_p1_each_day.append(row)
    for i in range(len(b1_y_p1_each_day)):
        b1_y_p1_each_day[i] = list(map(float,b1_y_p1_each_day[i]))
with open('feeding_tt/b1yp2.csv', 'r') as f:
    for row in csv.reader(f):
        b1_y_p2_each_day.append(row)
    for i in range(len(b1_y_p2_each_day)):
        b1_y_p2_each_day[i] = list(map(float,b1_y_p2_each_day[i]))
#--
with open('feeding_tt/b3xp1.csv', 'r') as f:
    for row in csv.reader(f):
        b3_x_p1_each_day.append(row)
    for i in range(len(b3_x_p1_each_day)):
        b3_x_p1_each_day[i] = list(map(float,b3_x_p1_each_day[i]))
with open('feeding_tt/b3xp2.csv', 'r') as f:
    for row in csv.reader(f):
        b3_x_p2_each_day.append(row)
    for i in range(len(b3_x_p2_each_day)):
        b3_x_p2_each_day[i] = list(map(float,b3_x_p2_each_day[i]))
with open('feeding_tt/b3yp1.csv', 'r') as f:
    for row in csv.reader(f):
        b3_y_p1_each_day.append(row)
    for i in range(len(b3_y_p1_each_day)):
        b3_y_p1_each_day[i] = list(map(float,b3_y_p1_each_day[i]))
with open('feeding_tt/b3yp2.csv', 'r') as f:
    for row in csv.reader(f):
        b3_y_p2_each_day.append(row)
    for i in range(len(b3_y_p2_each_day)):
        b3_y_p2_each_day[i] = list(map(float,b3_y_p2_each_day[i]))
#--
with open('feeding_tt/c1xp1.csv', 'r') as f:
    for row in csv.reader(f):
        c1_x_p1_each_day.append(row)
    for i in range(len(c1_x_p1_each_day)):
        c1_x_p1_each_day[i] = list(map(float,c1_x_p1_each_day[i]))
with open('feeding_tt/c1xp2.csv', 'r') as f:
    for row in csv.reader(f):
        c1_x_p2_each_day.append(row)
    for i in range(len(c1_x_p2_each_day)):
        c1_x_p2_each_day[i] = list(map(float,c1_x_p2_each_day[i]))
with open('feeding_tt/c1yp1.csv', 'r') as f:
    for row in csv.reader(f):
        c1_y_p1_each_day.append(row)
    for i in range(len(c1_y_p1_each_day)):
        c1_y_p1_each_day[i] = list(map(float,c1_y_p1_each_day[i]))
with open('feeding_tt/c1yp2.csv', 'r') as f:
    for row in csv.reader(f):
        c1_y_p2_each_day.append(row)
    for i in range(len(c1_y_p2_each_day)):
        c1_y_p2_each_day[i] = list(map(float,c1_y_p2_each_day[i]))
#--
with open('feeding_tt/c3xp1.csv', 'r') as f:
    for row in csv.reader(f):
        c3_x_p1_each_day.append(row)
    for i in range(len(c3_x_p1_each_day)):
        c3_x_p1_each_day[i] = list(map(float,c3_x_p1_each_day[i]))
with open('feeding_tt/c3xp2.csv', 'r') as f:
    for row in csv.reader(f):
        c3_x_p2_each_day.append(row)
    for i in range(len(c3_x_p2_each_day)):
        c3_x_p2_each_day[i] = list(map(float,c3_x_p2_each_day[i]))
with open('feeding_tt/c3yp1.csv', 'r') as f:
    for row in csv.reader(f):
        c3_y_p1_each_day.append(row)
    for i in range(len(c3_y_p1_each_day)):
        c3_y_p1_each_day[i] = list(map(float,c3_y_p1_each_day[i]))
with open('feeding_tt/c3yp2.csv', 'r') as f:
    for row in csv.reader(f):
        c3_y_p2_each_day.append(row)
    for i in range(len(c3_y_p2_each_day)):
        c3_y_p2_each_day[i] = list(map(float,c3_y_p2_each_day[i]))
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#%%
#==============================================================================
# fig = plt.figure()
# 
# a2p1 = fig.add_subplot(3,4,1)
# a2p1.scatter(a2_x_p1_each_day, a2_y_p1_each_day)
# 
# a2p2 = fig.add_subplot(3,4,2)
# a2p2.scatter(a2_x_p2_each_day, a2_y_p2_each_day)
# 
# a3p1 = fig.add_subplot(3,4,3)
# a3p1.scatter(a3_x_p1_each_day, a3_y_p1_each_day)
# 
# a3p2 = fig.add_subplot(3,4,4)
# a3p2.scatter(a3_x_p2_each_day, a3_y_p2_each_day)
# 
# b1p1 = fig.add_subplot(3,4,5)
# b1p1.scatter(b1_x_p1_each_day, b1_y_p1_each_day)
# 
# b1p2 = fig.add_subplot(3,4,6)
# b1p2.scatter(b1_x_p2_each_day, b1_y_p2_each_day)
# 
# b3p1 = fig.add_subplot(3,4,7)
# b3p1.scatter(b3_x_p1_each_day, b3_y_p1_each_day)
# 
# b3p2 = fig.add_subplot(3,4,8)
# b3p2.scatter(b3_x_p2_each_day, b3_y_p2_each_day)
# 
# c1p1 = fig.add_subplot(3,4,9)
# c1p1.scatter(c1_x_p1_each_day, c1_y_p1_each_day)
# 
# c1p2 = fig.add_subplot(3,4,10)
# c1p2.scatter(c1_x_p2_each_day, c1_y_p2_each_day)
# 
# c3p1 = fig.add_subplot(3,4,11)
# c3p1.scatter(c3_x_p1_each_day, c3_y_p1_each_day)
# 
# c3p2 = fig.add_subplot(3,4,12)
# c3p2.scatter(c3_x_p2_each_day, c3_y_p2_each_day)
# 
# plt.ion()
# plt.show()
#==============================================================================
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#-------import all done-------------------------------------------------------#
#%%-----build A2_p1 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(a2_x_p1_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:a2_x_p1_each_day, ys:a2_y_p1_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:a2_x_p1_each_day, ys:a2_y_p1_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:a2_x_p1_each_day, ys:a2_y_p1_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:a2_x_p1_each_day, ys:a2_y_p1_each_day})
    print(sess.run(loss,feed_dict={xs:a2_x_p1_each_day, ys:a2_y_p1_each_day}))
    prediction_value_a2p1 = sess.run(prediction, feed_dict={xs:a2_x_p1_test})         
#
#%%-----build A2_p2 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(a2_x_p2_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:a2_x_p2_each_day, ys:a2_y_p2_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:a2_x_p2_each_day, ys:a2_y_p2_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:a2_x_p2_each_day, ys:a2_y_p2_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:a2_x_p2_each_day, ys:a2_y_p2_each_day})
    print(sess.run(loss,feed_dict={xs:a2_x_p2_each_day, ys:a2_y_p2_each_day}))
    prediction_value_a2p2 = sess.run(prediction, feed_dict={xs:a2_x_p2_test})         
#
#%%-----build A3_p1 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(a3_x_p1_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:a3_x_p1_each_day, ys:a3_y_p1_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:a3_x_p1_each_day, ys:a3_y_p1_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:a3_x_p1_each_day, ys:a3_y_p1_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:a3_x_p1_each_day, ys:a3_y_p1_each_day})
    print(sess.run(loss,feed_dict={xs:a3_x_p1_each_day, ys:a3_y_p1_each_day}))
    prediction_value_a3p1 = sess.run(prediction, feed_dict={xs:a3_x_p1_test})         
#
#%%-----build A3_p2 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(a3_x_p2_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:a3_x_p2_each_day, ys:a3_y_p2_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:a3_x_p2_each_day, ys:a3_y_p2_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:a3_x_p2_each_day, ys:a3_y_p2_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:a3_x_p2_each_day, ys:a3_y_p2_each_day})
    print(sess.run(loss,feed_dict={xs:a3_x_p2_each_day, ys:a3_y_p2_each_day}))
    prediction_value_a3p2 = sess.run(prediction, feed_dict={xs:a3_x_p2_test})         
#
#%%-----build B1_p1 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(b1_x_p1_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:b1_x_p1_each_day, ys:b1_y_p1_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:b1_x_p1_each_day, ys:b1_y_p1_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:b1_x_p1_each_day, ys:b1_y_p1_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:b1_x_p1_each_day, ys:b1_y_p1_each_day})
    print(sess.run(loss,feed_dict={xs:b1_x_p1_each_day, ys:b1_y_p1_each_day}))
    prediction_value_b1p1 = sess.run(prediction, feed_dict={xs:b1_x_p1_test})         
#
#%%-----build B1_p2 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(b1_x_p2_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:b1_x_p2_each_day, ys:b1_y_p2_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:b1_x_p2_each_day, ys:b1_y_p2_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:b1_x_p2_each_day, ys:b1_y_p2_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:b1_x_p2_each_day, ys:b1_y_p2_each_day})
    print(sess.run(loss,feed_dict={xs:b1_x_p2_each_day, ys:b1_y_p2_each_day}))
    prediction_value_b1p2 = sess.run(prediction, feed_dict={xs:b1_x_p2_test})         
#
#%%-----build B3_p1 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(b3_x_p1_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:b3_x_p1_each_day, ys:b3_y_p1_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:b3_x_p1_each_day, ys:b3_y_p1_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:b3_x_p1_each_day, ys:b3_y_p1_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:b3_x_p1_each_day, ys:b3_y_p1_each_day})
    print(sess.run(loss,feed_dict={xs:b3_x_p1_each_day, ys:b3_y_p1_each_day}))
    prediction_value_b3p1 = sess.run(prediction, feed_dict={xs:b3_x_p1_test})         
#
#%%-----build B3_p2 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(b3_x_p2_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:b3_x_p2_each_day, ys:b3_y_p2_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:b3_x_p2_each_day, ys:b3_y_p2_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:b3_x_p2_each_day, ys:b3_y_p2_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:b3_x_p2_each_day, ys:b3_y_p2_each_day})
    print(sess.run(loss,feed_dict={xs:b3_x_p2_each_day, ys:b3_y_p2_each_day}))
    prediction_value_b3p2 = sess.run(prediction, feed_dict={xs:b3_x_p2_test})         
#
#%%-----build C1_p1 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(c1_x_p1_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:c1_x_p1_each_day, ys:c1_y_p1_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:c1_x_p1_each_day, ys:c1_y_p1_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:c1_x_p1_each_day, ys:c1_y_p1_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:c1_x_p1_each_day, ys:c1_y_p1_each_day})
    print(sess.run(loss,feed_dict={xs:c1_x_p1_each_day, ys:c1_y_p1_each_day}))
    prediction_value_c1p1 = sess.run(prediction, feed_dict={xs:c1_x_p1_test})         
#
#%%-----build C1_p2 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(c1_x_p2_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:c1_x_p2_each_day, ys:c1_y_p2_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:c1_x_p2_each_day, ys:c1_y_p2_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:c1_x_p2_each_day, ys:c1_y_p2_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:c1_x_p2_each_day, ys:c1_y_p2_each_day})
    print(sess.run(loss,feed_dict={xs:c1_x_p2_each_day, ys:c1_y_p2_each_day}))
    prediction_value_c1p2 = sess.run(prediction, feed_dict={xs:c1_x_p2_test})         
#
#%%-----build C3_p1 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(c3_x_p1_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:c3_x_p1_each_day, ys:c3_y_p1_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:c3_x_p1_each_day, ys:c3_y_p1_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:c3_x_p1_each_day, ys:c3_y_p1_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:c3_x_p1_each_day, ys:c3_y_p1_each_day})
    print(sess.run(loss,feed_dict={xs:c3_x_p1_each_day, ys:c3_y_p1_each_day}))
    prediction_value_c3p1 = sess.run(prediction, feed_dict={xs:c3_x_p1_test})         
#
#%%-----build C3_p2 nn and run it---------------------------------------------#
xs = tf.placeholder(tf.float32,[None,None])
ys = tf.placeholder(tf.float32,[None,None])

l1 = add_layer(xs, 6,  30, activation_function=tf.nn.relu)
l2 = add_layer(l1, 30,  20, activation_function=None)
prediction = add_layer(l2 , 20 , 6 , activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(c3_x_p2_each_day - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(0.005).minimize(loss)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(8000):
        sess.run(train_step, feed_dict={xs:c3_x_p2_each_day, ys:c3_y_p2_each_day})
        if i % 500 ==0:
            print(sess.run(loss,feed_dict={xs:c3_x_p2_each_day, ys:c3_y_p2_each_day}))
    print('--training schedule end--')
    while loss.eval(feed_dict={xs:c3_x_p2_each_day, ys:c3_y_p2_each_day}) > 0.5:
        sess.run(train_step, feed_dict={xs:c3_x_p2_each_day, ys:c3_y_p2_each_day})
    print(sess.run(loss,feed_dict={xs:c3_x_p2_each_day, ys:c3_y_p2_each_day}))
    prediction_value_c3p2 = sess.run(prediction, feed_dict={xs:c3_x_p2_test})         
#
#%%-------transform to submission format----------#
concate_data = np.concatenate((prediction_value_a2p1,prediction_value_a3p1,
                                  prediction_value_b1p1,prediction_value_b3p1,
                                  prediction_value_c1p1,prediction_value_c3p1,
                                  prediction_value_a2p2,prediction_value_a3p2,
                                  prediction_value_b1p2,prediction_value_b3p2,
                                  prediction_value_c1p2,prediction_value_c3p2))

submission_data = concate_data.reshape((504,1))

submission_data = list(map(float,submission_data))
for i in range(len(submission_data)):
    submission_data[i] = round(submission_data[i], 2)
#