# Generated by Django 3.2.8 on 2021-10-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='keyword1',
            field=models.CharField(default='', max_length=100),
        ),
    ]
