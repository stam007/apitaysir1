# Generated by Django 2.2.5 on 2019-09-07 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_reciverequest_date_send_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendrequest',
            name='type_Request',
            field=models.CharField(choices=[('Want Give Money', 'Want Give Money'), ('Want Take Money', 'Want Take Money')], max_length=20),
        ),
    ]
