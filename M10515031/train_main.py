import pandas as pd
import datetime
from sklearn import linear_model
import progressbar
#df = pd.read_csv('../dataSets/training/trajectories(table 5)_training.csv')
bar = progressbar.ProgressBar()


def train_model(f):
	#data X, Y
	df = pd.read_csv('t'+f+'.csv')
	df = df.dropna()
	X_columns = []
	for i in df.keys():
		X_columns.append(i)
	X_columns.remove('travel_time')
	

	X = df[X_columns]
	Y = df[['travel_time']]

	X_columns.remove('time_point')
	data = []
	for index, row in X.iterrows():
		nd = []
		time = row['time_point'].split(':')
		sum_time = float(time[1]) + float(time[2])/60
		nd.append(float(time[0]))
		nd.append(sum_time)

		for i in X_columns:
			nd.append(row[i])
		data.append(nd)
	X_columns = ['hours','time_point'] + X_columns
	X = pd.DataFrame(data, columns = X_columns)
	

	#create model
	reg = linear_model.LinearRegression()

	#model fit
	reg.fit(X, Y)
	return reg, X.describe(), X_columns


def divide( model, mean_list, X_columns, test):
	print X_columns
	data = []
	describe = ['25%','mean','50%','75%']
	time_range = 5
	iii = 0
	for index, row in test.iterrows():
		for k in range(time_range):
			nd = []
			time = row['time_window'].replace('[','').replace(')','').split(',')
			point = time[0].split(' ')[1].split(':')
			sum_time = float(point[1]) + float(point[2])/60 + k*4
			nd.append(float(point[0]))
			nd.append(sum_time)
			nd.append(datetime.datetime.strptime(time[0].split(' ')[0], '%Y-%m-%d').weekday())

			PK = []
			for i in mean_list.keys():
				PK.append(i)
			PK.remove('hours')
			PK.remove('time_point')
			PK.remove('weekend')
			for path in PK:
				nd.append(mean_list[path][describe[iii%4]])

			data.append(nd)
		iii += 1

	X = pd.DataFrame(data, columns = X_columns)
	ans = model.predict(X)
	f_ans = []
	for i in range(0,len(ans),time_range):
		total = .0
		for j in range(time_range):
			total += ans[i+j][0]
		total = total / time_range
		f_ans.append([total])
		
	return f_ans


def main():
	all_model = {'A2':0,'A3':0,'B1':0,'B3':0,'C1':0,'C3':0}
	df = pd.read_csv('submission.csv')
	
	for i in all_model.keys():
		all_model[i] = train_model(i)
	
	
	df = pd.read_csv('submission.csv')
	print df.describe()
	data = []
	allans = []
	for i in all_model.keys():
		p = df[ df['intersection_id'] == i[0]]
		p = p[ p['tollgate_id'] == int(i[1]) ]
		ans = divide(all_model[i][0], all_model[i][1], all_model[i][2], p)
		for j in ans:
			allans.append(j)


	X = pd.DataFrame(allans)
	X.to_csv('ans.csv')











if __name__ == '__main__':
	main()
