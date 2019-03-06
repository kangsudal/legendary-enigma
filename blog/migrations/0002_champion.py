# Generated by Django 2.1.4 on 2019-03-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('unnamed_0', models.BigIntegerField(blank=True, db_column='Unnamed: 0', null=True)),
                ('version', models.TextField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('key', models.BigIntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('blurb', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('partype', models.TextField(blank=True, null=True)),
                ('attack', models.BigIntegerField(blank=True, null=True)),
                ('defense', models.BigIntegerField(blank=True, null=True)),
                ('magic', models.BigIntegerField(blank=True, null=True)),
                ('difficulty', models.BigIntegerField(blank=True, null=True)),
                ('tag1', models.TextField(blank=True, null=True)),
                ('tag2', models.TextField(blank=True, null=True)),
                ('hp', models.FloatField(blank=True, null=True)),
                ('hpperlevel', models.FloatField(blank=True, null=True)),
                ('mp', models.FloatField(blank=True, null=True)),
                ('mpperlevel', models.FloatField(blank=True, null=True)),
                ('movespeed', models.FloatField(blank=True, null=True)),
                ('armor', models.FloatField(blank=True, null=True)),
                ('armorperlevel', models.FloatField(blank=True, null=True)),
                ('spellblock', models.FloatField(blank=True, null=True)),
                ('spellblockperlevel', models.FloatField(blank=True, null=True)),
                ('attackrange', models.FloatField(blank=True, null=True)),
                ('hpregen', models.FloatField(blank=True, null=True)),
                ('hpregenperlevel', models.FloatField(blank=True, null=True)),
                ('mpregen', models.FloatField(blank=True, null=True)),
                ('mpregenperlevel', models.FloatField(blank=True, null=True)),
                ('crit', models.FloatField(blank=True, null=True)),
                ('critperlevel', models.FloatField(blank=True, null=True)),
                ('attackdamage', models.FloatField(blank=True, null=True)),
                ('attackdamageperlevel', models.FloatField(blank=True, null=True)),
                ('attackspeedperlevel', models.FloatField(blank=True, null=True)),
                ('attackspeed', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'champion',
            },
        ),
    ]
