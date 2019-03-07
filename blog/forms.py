from django import forms

from .models import Post
from .models import Champion
import requests
from django.db.models import Q

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



        if defense is None and attack is None and magic is None and difficulty is None:
            result = None
            return result

        c = Champion.objects.all()

        if defense:
            c = c.filter(defense=defense)
        if attack:
            c = c.filter(attack=attack)
        if magic:
            c = c.filter(magic=magic)
        if difficulty:
            c = c.filter(difficulty=difficulty)

        result = c
    
        return result
