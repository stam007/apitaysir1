# Generated by Django 2.2.5 on 2019-09-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0033_auto_20190910_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='imageurl',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]