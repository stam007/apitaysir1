# Generated by Django 2.2.5 on 2019-09-08 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0019_auto_20190909_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendrequest',
            name='Is_Readed',
        ),
        migrations.RemoveField(
            model_name='sendrequest',
            name='Is_See',
        ),
        migrations.RemoveField(
            model_name='sendrequest',
            name='id_User_Giver',
        ),
        migrations.RemoveField(
            model_name='sendrequest',
            name='id_User_Taken',
        ),
    ]
