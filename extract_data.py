import hashlib
import pymongo
import sys
import os
import pandas as pd

# hashlib.md5(name.encode()).hexdigest()

client = pymongo.MongoClient(
    'mongodb+srv://CacsMaster:T99bxZ9cvOjz409O@cacsws.7tsho.mongodb.net/cacsws?retryWrites=true&w=majority')
db = client['cacs']
cacs_api = client['cacs_api']


def write_users(file_name):
	print(file_name)
	df = pd.read_excel(file_name, header=None)
	result = pd.DataFrame()

	df.columns = ['name', 'time', 'audit', 'form', 'mark', 'mark_text', 'date', 'empt', 'descr']
	print(df)
	last_line = df.shape[0]
	print(last_line)
	samp = list(df['name'][df['name'] == 'Фамилия, имя, отчество'].index)
	samp.append(last_line)
	# print(samp)

	for i in range(len(samp) - 1):
		try:
			frame = df.iloc[samp[i]:samp[i + 1]]
			index = list(frame['name'][frame['name'] == 'Название  предмета'].index)
			index.append(samp[i + 1])
			name = frame.iloc[0]['time'] + ' ' + frame.iloc[0]['audit'] + ' ' + frame.iloc[0]['form']
			birth = frame.iloc[1]['time'].split('.')[2].split()[0]
			contract = frame.iloc[2]['time']
			print('(', i+1, '/', len(samp) - 1, ')', ' ', name, sep='')
			user_lessons = {'user': name, 'birth': birth, 'contract': contract, 'group': file_name.split('.')[0]}

			for j in range(len(index)-1):
				lessons = frame.loc[index[j]:index[j+1]]
				for k in range(lessons.shape[0]):
					if type(lessons.iloc[k]['mark']) == str and lessons.iloc[k]['mark'][0] in ["1", '2', '3', '4', '5', 1, 2, 3, 4, 5]:
						string = lessons.iloc[k]
						user_lessons[string['name'].strip() + ' ' + string['form'].strip() + ' ' + frame.loc[index[j]-1]['name'][-10]] =  string['mark']
			result = result.append(user_lessons, ignore_index=True)
		except Exception as e:
			print(e)
			pass
	result.to_excel('res_'+file_name)
	return 1


def hash_our_users():
	users = list(cacs_api.users.find({'role': 'student'}))
	for i in users:
		name = i['name'].split()
		if len(name) > 2:
			name = name[0] + ' ' + name[1][0] + '.' + name[2][0] + '.'
		else:
			name = name[0] + ' ' + name[1][0] + '.'
		print('(', users.index(i)+1, '/', len(users), ')', ' ', name, sep='')
		cacs_api.users.update_one(i, {'$set': {'hash': hashlib.md5(name.encode()).hexdigest()}})


def hash_table_users(file_name):
	df = pd.read_excel(file_name, index_col='Unnamed: 0')
	df['short_name'] = df.apply(axis=1, func=lambda x: x['user'].split()[0] + ' ' + x['user'].split()[1][0] + '.' + x['user'].split()[2][0] + '.' if len(x['user'].split()) > 2 else x['user'].split()[0] + ' ' + x['user'].split()[1][0] + '.')
	df['hash'] = df.apply(axis=1, func=lambda x: hashlib.md5(x['short_name'].encode()).hexdigest())
	df.drop(['user', 'short_name'], axis=1, inplace=True)
	df.to_excel('saved/hash_' + file_name)


def decode_users(file_name):
	users = list(cacs_api.users.find({'role': 'student'}))
	df = pd.read_excel('./saved/' + file_name, index_col='Unnamed: 0')
	df['name'] = df.apply(lambda x: [i for i in users if str(i['hash']) == str(x['hash'])][0]['name'], axis=1)
	df.to_excel('saved/rdy/' + 'result_' + file_name)


if __name__ == '__main__':
	# filename = sys.argv[1]
	# print('start')
	# write_users(filename)
	# print('1 cont')
	# hash_our_users()
	# hash_table_users('res_' + filename)
	# print('2 cont')
	if 'rdy' not in os.listdir('./saved/'):
		os.mkdir('./saved/rdy')
	for i in os.listdir('./saved/'):
		print(i)
		decode_users(i)
	# print('rdy')