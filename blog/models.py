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

# class Champion(models.Model):
#     version = models.FloatField()
#     id = models.CharField(max_length=100, primary_key=True)
#     key = models.CharField(max_length=100)  
#     name = models.CharField(max_length=100)   
#     title = models.CharField(max_length=100)
#     blurb = models.CharField(max_length=1000)
#     image = models.CharField(max_length=100)
#     partype = models.CharField(max_length=100)
#     attack  = models.IntegerField()
#     defense = models.IntegerField()
#     magic= models.IntegerField()
#     difficulty = models.IntegerField() 
#     tag1 = models.CharField(max_length=100)
#     tag2 = models.CharField(max_length=100)
#     hp  = models.FloatField()
#     hpperlevel = models.FloatField() 
#     mp  = models.FloatField()
#     mpperlevel  = models.FloatField()
#     movespeed   = models.FloatField()
#     armor   = models.FloatField()
#     armorperlevel   = models.FloatField()
#     spellblock  = models.FloatField()
#     spellblockperlevel  = models.FloatField()
#     attackrange = models.FloatField()
#     hpregen = models.FloatField()
#     hpregenperlevel = models.FloatField()
#     mpregen = models.FloatField()
#     mpregenperlevel = models.FloatField()
#     crit= models.FloatField()
#     critperlevel= models.FloatField()
#     attackdamage= models.FloatField()
#     attackdamageperlevel= models.FloatField()
#     attackspeedperlevel = models.FloatField()
#     attackspeed= models.FloatField()

class Champion(models.Model):
    unnamed_0 = models.BigIntegerField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.TextField(blank=True, null=True)
    id = models.TextField(blank=True, primary_key=True)
    key = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    partype = models.TextField(blank=True, null=True)
    attack = models.BigIntegerField(blank=True, null=True)
    defense = models.BigIntegerField(blank=True, null=True)
    magic = models.BigIntegerField(blank=True, null=True)
    difficulty = models.BigIntegerField(blank=True, null=True)
    tag1 = models.TextField(blank=True, null=True)
    tag2 = models.TextField(blank=True, null=True)
    hp = models.FloatField(blank=True, null=True)
    hpperlevel = models.FloatField(blank=True, null=True)
    mp = models.FloatField(blank=True, null=True)
    mpperlevel = models.FloatField(blank=True, null=True)
    movespeed = models.FloatField(blank=True, null=True)
    armor = models.FloatField(blank=True, null=True)
    armorperlevel = models.FloatField(blank=True, null=True)
    spellblock = models.FloatField(blank=True, null=True)
    spellblockperlevel = models.FloatField(blank=True, null=True)
    attackrange = models.FloatField(blank=True, null=True)
    hpregen = models.FloatField(blank=True, null=True)
    hpregenperlevel = models.FloatField(blank=True, null=True)
    mpregen = models.FloatField(blank=True, null=True)
    mpregenperlevel = models.FloatField(blank=True, null=True)
    crit = models.FloatField(blank=True, null=True)
    critperlevel = models.FloatField(blank=True, null=True)
    attackdamage = models.FloatField(blank=True, null=True)
    attackdamageperlevel = models.FloatField(blank=True, null=True)
    attackspeedperlevel = models.FloatField(blank=True, null=True)
    attackspeed = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'champion'


    def __str__(self):
        return self.name    