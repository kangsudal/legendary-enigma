from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Champion(models.Model):
    version = models.FloatField()
    id = models.CharField(max_length=100, primary_key=True)
    key = models.CharField(max_length=100)  
    name = models.CharField(max_length=100)   
    title = models.CharField(max_length=100)
    blurb = models.CharField(max_length=1000)
    image = models.CharField(max_length=100)
    partype = models.CharField(max_length=100)
    attack  = models.IntegerField()
    defense = models.IntegerField()
    magic= models.IntegerField()
    difficulty = models.IntegerField() 
    tag1 = models.CharField(max_length=100)
    tag2 = models.CharField(max_length=100)
    hp  = models.FloatField()
    hpperlevel = models.FloatField() 
    mp  = models.FloatField()
    mpperlevel  = models.FloatField()
    movespeed   = models.FloatField()
    armor   = models.FloatField()
    armorperlevel   = models.FloatField()
    spellblock  = models.FloatField()
    spellblockperlevel  = models.FloatField()
    attackrange = models.FloatField()
    hpregen = models.FloatField()
    hpregenperlevel = models.FloatField()
    mpregen = models.FloatField()
    mpregenperlevel = models.FloatField()
    crit= models.FloatField()
    critperlevel= models.FloatField()
    attackdamage= models.FloatField()
    attackdamageperlevel= models.FloatField()
    attackspeedperlevel = models.FloatField()
    attackspeed= models.FloatField()

