import csv
import requests

VERSION = '9.2.1' #https://ddragon.leagueoflegends.com/api/versions.json
URL = 'http://ddragon.leagueoflegends.com/cdn/'+VERSION+'/data/en_US/champion.json'




def load_JSON():
	data = {}
	
	response = requests.get(URL)
	data = response.json()

	return data

# def saveAs_CSV():
# 	data_dict = load_JSON()

# 	keys = data_dict['data']['Aatrox'].keys()

# 	names = data_dict['data'].keys()

# 	with open('version'+VERSION+'.csv', 'w', encoding='utf-8', newline='') as csvfile:
# 	    fieldnames = keys
# 	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

# 	    writer.writeheader()
# 	    for name in names:
# 	    	writer.writerow(data_dict['data'][name])


def saveAs_CSV():
	data_dict = load_JSON()

	keys = data_dict['data']['Aatrox'].keys()
	# print(type(keys))

	#추가할 column 요소 체크(이 코드가 없어도 실행됨)
	for key, value in data_dict['data']['Aatrox'].items():
		print(value,type(value))
		if type(value) is dict or type(value) is list:
			print('you should separate this','and this key is **',key,'len is',len(value))
			# keys.add(key)

	names = data_dict['data'].keys()

	with open('version'+VERSION+'.csv', 'w', encoding='utf-8', newline='') as csvfile:
	    fieldnames = keys
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	    writer.writeheader()
	    for name in names:
	    	writer.writerow(data_dict['data'][name])	  
	    	


if __name__ == '__main__':
	data_dict = {}
	saveAs_CSV()
