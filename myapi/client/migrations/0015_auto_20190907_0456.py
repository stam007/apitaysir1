# Generated by Django 2.2.5 on 2019-09-07 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20190907_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciverequest',
            name='Accepted_Status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
