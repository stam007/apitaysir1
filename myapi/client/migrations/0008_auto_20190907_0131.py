# Generated by Django 2.2.5 on 2019-09-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20190907_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendrequest',
            name='Date_Send_Request',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
