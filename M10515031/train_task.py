import pandas as pd
import datetime
#df = pd.read_csv('../dataSets/training/trajectories(table 5)_training.csv')

def train_out(f):
	df = pd.read_csv('p'+f+'.csv')

	columns = ['weekend', 'time_point', 'travel_time']
	road = df.loc()[1]['travel_seq']
	for i in road.split(';'):
		info = i.split('#')
		columns.append(info[0])

	data = []

	print columns

	for index , row in df.iterrows():
	 	row_data = []
	 	st = row['starting_time'].split(' ')
	 	#weekend
	 	row_data.append(datetime.datetime.strptime(st[0], '%Y-%m-%d').weekday())
	 	#time_point
	 	row_data.append(st[1])
	 	

	 	#travel_time
	 	tt = row['travel_time']
	 	row_data.append(tt)

	 	#road_list
	 	ts = row['travel_seq']
	 	for i in ts.split(';'):
			info = i.split('#')
			row_data.append(info[2])
	 	data.append(row_data)

	 			
	train_data = pd.DataFrame(data, columns = columns)
	train_data.to_csv('t'+ f +'.csv', index = False)



all_path = [['A',2],['A',3],['B',1],['B',3],['C',1],['C',3]]
for i in all_path:
	train_out(i[0]+str(i[1]))