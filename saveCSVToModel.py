'''
csv -> dataframe -> django model(db)

https://creativedata.atlassian.net/wiki/spaces/SAP/pages/130318375/Python+-+Read+Write+tables+from+PostgreSQL+with+Security

https://stackoverflow.com/questions/34425607/how-to-write-a-pandas-dataframe-to-django-model
https://stackoverflow.com/questions/37688054/saving-a-pandas-dataframe-to-a-django-model

'''

import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine


import os

#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
#from blog.models import Champion

VERSION = '9.2.1'

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

#print(user,password,database_name)

#postgresql에 연결
database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)
engine = create_engine(database_url, echo=False)


df_input = pd.read_csv('finished_version'+VERSION+'.csv')
#print(list(df_input))
# 데이터프레임 postgresql에 저장
df_input.to_sql(
	name='champion', #mysite_db데이터베이스 안에 table 이름
	con=engine, 
	index=False,
	if_exists='replace')


#engine.execute('select * from mysite_db').fetchall()

#data = pd.read_sql('SELECT * FROM champion', engine)
#print('data:',data)


# django inspectdb specific table
#https://stackoverflow.com/questions/27163702/how-do-i-inspectdb-1-table-from-database-which-contains-1000-tables
import subprocess
subprocess.run(["python","manage.py","inspectdb","champion"])