import pandas as pd
df = pd.read_csv('../dataSets/training/trajectories(table 5)_training.csv')

def cut(I_id, T_id):
	#print "Mean ",df.describe()['tollgate_id']['mean']

	p = df[ df['intersection_id'] == I_id]
	p = p[ p['tollgate_id'] == T_id ]
	p.to_csv( 'p' + I_id + str(T_id) + '.csv', index=False)



all_path = [['A',2],['A',3],['B',1],['B',3],['C',1],['C',3]]
for i in all_path:
	cut(i[0],i[1])