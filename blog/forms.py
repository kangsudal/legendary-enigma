from django import forms

from .models import Post
import requests

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class SearchByStatForm(forms.Form):

    defense = forms.IntegerField(label='방어', required=False)
    attack= forms.IntegerField(label='공격', required=False)
    magic= forms.IntegerField(label='마법', required=False)
    difficulty= forms.IntegerField(label='난이도', required=False)


    def search(self):
        result = {}

        defense = self.cleaned_data['defense']
        attack = self.cleaned_data['attack']
        magic = self.cleaned_data['magic']
        difficulty = self.cleaned_data['difficulty']

        url = 'http://ddragon.leagueoflegends.com/cdn/9.1.1/data/en_US/champion.json'
        response = requests.get(url)
        champion_data = response.json()
        champions = champion_data['data']    	

    	# for key, value in champions.items() :
    	# 	print(key,value)

    	#print(list(champions.items()))
    	#a = filter(positive, champions.)

    	# a = filter(positive, li)
        conditions =[defense,attack,magic,difficulty]
    	#result = filter(positive, champions)

        result = self.getKeysByValues(champions, conditions)

        #print(result)

        return result

    def getKeysByValues(self, champions, list):
        champDics={}

        for key,value in champions.items():
            if self.isSame(value['info']['defense'], list[0]) and self.isSame(value['info']['attack'], list[1]) and self.isSame(value['info']['magic'], list[2]) and self.isSame(value['info']['difficulty'], list[3]) :
                champDics.update({key:value})
             
	                
        return champDics

    def isSame( self, data, condition):
        if condition is None:
            return True

        if data is condition:
            return True

        return False    