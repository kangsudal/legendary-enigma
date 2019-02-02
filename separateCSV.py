'''
필요한 column: attack	defense	magic	difficulty	tag1	tag2 
뽑아내는 코드
'''
import ast
import pandas as pd

VERSION = '9.2.1'

def brush(df_input):

	#str로 쓰여있는
	#{'attack': 8, 'defense': 4, 'magic': 3, 'difficulty': 4} 를 진짜 dict로 변환
	df_input['info'] = df_input['info'].map(ast.literal_eval)
	

	#info값 쪼개기
	df_input['info'].apply(pd.Series)
	'''
	0      {'attack': 8, 'defense': 4, 'magic': 3, 'diffi...
	1      {'attack': 3, 'defense': 4, 'magic': 8, 'diffi...
	2      {'attack': 5, 'defense': 3, 'magic': 8, 'diffi...
	->
	Name: info, Length: 143, dtype: object
	     attack  defense  magic  difficulty
	0         8        4      3           4
	1         3        4      8           5
	2         5        3      8           7
	'''	
	df_result = pd.concat( [df_input.drop(['info'], axis=1), df_input['info'].apply(pd.Series)], axis=1)

	return df_result


def brush2(df_input):
	#데이터 형태를 str에서 list로 변환
	df_input['tags'] = df_input['tags'].map(ast.literal_eval)
	

	#tags값 쪼개기
	df2 = df_input['tags'].apply(pd.Series)
	df2.columns = ['tag1', 'tag2']
	# print( df2 )
	'''
	tags
	['Fighter', 'Tank']
	['Mage', 'Assassin']
	['Assassin']
	['Tank', 'Support']
	['Tank', 'Mage']

	->
	            0         1
	0     Fighter      Tank
	1        Mage  Assassin
	2    Assassin       NaN
	3        Tank   Support
	4        Tank      Mage
	'''	
	df1 = df_input.drop(['tags'], axis=1)
	df_result = pd.concat( [ df1 , df2 ], axis=1)

	return df_result

def brush3(df_input):

	#str로 쓰여있는
	#{'hp': 580, 'hpperlevel': 80, 'mp': 0, 'mpperlevel': 0, 'movespeed': 345, 'armor': 33, 'armorperlevel': 3.25, 'spellblock': 32.1, 'spellblockperlevel': 1.25, 'attackrange': 175, 'hpregen': 5, 'hpregenperlevel': 0.25, 'mpregen': 0, 'mpregenperlevel': 0, 'crit': 0, 'critperlevel': 0, 'attackdamage': 60, 'attackdamageperlevel': 5, 'attackspeedperlevel': 2.5, 'attackspeed': 0.651} 를 진짜 dict로 변환
	df_input['stats'] = df_input['stats'].map(ast.literal_eval)
	

	#info값 쪼개기
	df2 = df_input['stats'].apply(pd.Series)

	df1 = df_input.drop(['stats'], axis=1)
	df_result = pd.concat( [ df1, df2 ], axis=1)

	return df_result

if __name__ == '__main__':

	#저장된 데이터를 불러들여서 
	df_input = pd.read_csv('version'+VERSION+'.csv')

	
	df = brush(df_input)

	df = brush2(df)

	df_output = brush3(df)
	
	
	#DataFrame을 csv파일로 저장
	df_output.to_csv('finished_version'+VERSION+'.csv', encoding='utf-8')
