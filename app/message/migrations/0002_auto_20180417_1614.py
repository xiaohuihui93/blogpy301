# Generated by Django 2.0.4 on 2018-04-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False, verbose_name='zhujian'),
        ),
    ]
