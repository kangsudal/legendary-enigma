'''
separateCSV.py로 만들어진 finished_version.csv데이터를 이용해서 
lv.1~ lv.18 hp같은 스텟 데이터를 표로 만드는것

'''
import ast
import pandas as pd

VERSION = '9.2.1'


def perlevelstatsmultiplier(df_input):
	df_result = pd.DataFrame(df_input[['name','hp','hpperlevel']])

	for i in range(1,19):
		df_result[i] = df_result['hp']+df_result['hpperlevel']*(i-1)


	return df_result


if __name__ == '__main__':

	#저장된 데이터를 불러들여서 
	df_input = pd.read_csv('finished_version'+VERSION+'.csv')

	
	df_output = perlevelstatsmultiplier(df_input)
	
	
	#DataFrame을 csv파일로 저장
	df_output.to_csv('statsTable_version'+VERSION+'.csv', encoding='utf-8')
