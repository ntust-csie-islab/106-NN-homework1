#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:48:25 2017

@author: Mark1002
"""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
# from sklearn.metrics import mean_squared_error

def select_route(df, route_tuple):
    intersection_id = route_tuple[0]
    tollgate_id = route_tuple[1]

    df = df.loc[(df['intersection_id'] == intersection_id) & 
                (df['tollgate_id'] == tollgate_id),:]
    series = pd.Series(df['avg_travel_time'].values, 
                       index=df['time_window'].values)
    return series

def regular_time(df):
    # 將 time_window 轉成單一時間
    df['time_window'] = pd.to_datetime(
        df['time_window'].str.split(',').str[0].str.replace('[','')
        )

test_data = pd.read_csv('test1_20min_avg_travel_time.csv')
train_data = pd.read_csv('training_20min_avg_travel_time.csv')

regular_time(test_data)
regular_time(train_data)

result_df = pd.DataFrame(
        columns = ['intersection_id','tollgate_id', 
                   'time_window','avg_travel_time']
        )
# A,3 A,2 B,1 B,3 C,1 C,3
route_list = [('A', 3), ('A', 2), ('B', 1), ('B', 3), ('C', 1), ('C', 3)]

date_list = ['2016-10-18', '2016-10-19', '2016-10-20', '2016-10-21', 
        '2016-10-22', '2016-10-23', '2016-10-24']

hour_min_list = [
            {'start': '08:00:00', 'end': '09:40:00'}, 
            {'start': '17:00:00', 'end': '18:40:00'}
            ]

for route in route_list:
    # test_series = select_route(test_data, route)
    train_series = select_route(train_data, route)
    for date in date_list:
        for hour_min in hour_min_list:
            start = date + ' ' + hour_min['start']
            end = date + ' ' + hour_min['end']
            train_series_interval = train_series.between_time(hour_min['start'], 
                                                              hour_min['end'])
            model = ARIMA(train_series_interval, order=(5,1,0))
            model_fit = model.fit(disp=0)
            
            rng = pd.date_range(start, end, freq='20min')
            predictions = pd.Series(model_fit.forecast(steps=len(rng))[0].tolist(),
                                    index = rng)
            
            # error = mean_squared_error(test_series[start:end], predictions[start:end])
            # print('Test MSE: %.3f' % error)
            df = pd.DataFrame({'intersection_id':route[0], 
                               'tollgate_id':str(route[1]), 
                               'time_window':predictions[start:end].index, 
                               'avg_travel_time':predictions[start:end].values},
                                columns = ['intersection_id','tollgate_id', 
                                           'time_window','avg_travel_time'])
            result_df = result_df.append(df, ignore_index=True)
            
window_start = result_df['time_window'].astype(str)
window_end = (result_df['time_window'] + pd.Timedelta(minutes=20)).astype(str)
result_df['time_window'] = '[' + window_start + ',' + window_end + ')'
result_df.to_csv('travel_time_result.csv',index=False)