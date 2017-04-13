#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 11:13:46 2017

@author: Mark1002
"""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

def select_direction(df, d):
    df = df.loc[(df['tollgate_id']==d['id']) & 
                (df['direction']==d['direction']),:]
    series = pd.Series(df['volume'].values.astype(float), index=df['time_window'])
    return(series)

def regular_time(df):
    # 將 time_window 轉成單一時間
    df['time_window'] = pd.to_datetime(
        df['time_window'].str.split(',').str[0].str.replace('[','')
        )
    
train_data = pd.read_csv('training_20min_avg_volume.csv')
regular_time(train_data)

result_df = pd.DataFrame(
        columns = ['tollgate_id', 'time_window', 'direction', 'volume']
        )

#1-entry, 1-exit, 2-entry, 3-entry and 3-exit
volume_list = [
        {'id':1, 'direction':0}, 
        {'id':1, 'direction':1},
        {'id':2, 'direction':0},
        {'id':3, 'direction':0},
        {'id':3, 'direction':1}]

date_list = ['2016-10-18', '2016-10-19', '2016-10-20', '2016-10-21', 
        '2016-10-22', '2016-10-23', '2016-10-24']

hour_min_list = [
            {'start': '08:00:00', 'end': '09:40:00'}, 
            {'start': '17:00:00', 'end': '18:40:00'}
            ]

for volume_el in volume_list:
    train_series = select_direction(train_data, volume_el)
    for date in date_list:
        for hour_min in hour_min_list:
            start = date + ' ' + hour_min['start']
            end = date + ' ' + hour_min['end']
            train_series_interval = train_series.between_time(hour_min['start'],
                                                              hour_min['end'])
            
            model = ARIMA(train_series_interval, order=(5,1,0))
            model_fit = model.fit(disp=0)          
            rng = pd.date_range(start, end, freq='20min')
            predictions = pd.Series(model_fit.forecast(steps=len(rng))[0].tolist(), index = rng)
            
            df = pd.DataFrame({'tollgate_id':str(volume_el['id']), 
                               'time_window':predictions[start:end].index, 
                               'direction':str(volume_el['direction']),
                               'volume':predictions[start:end].values.astype(int)},
                                columns = ['tollgate_id', 'time_window', 
                                           'direction', 'volume'])
            
            result_df = result_df.append(df, ignore_index=True)

window_start = result_df['time_window'].astype(str)
window_end = (result_df['time_window'] + pd.Timedelta(minutes=20)).astype(str)
result_df['time_window'] = '[' + window_start + ',' + window_end + ')'
    
result_df.to_csv('volume_result.csv', index=False)   