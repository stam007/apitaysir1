# Generated by Django 2.2.5 on 2019-09-09 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0026_auto_20190909_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendrequest',
            name='id_User_Reciver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reciveuser+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sendrequest',
            name='id_User_Sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='senduser+', to=settings.AUTH_USER_MODEL),
        ),
    ]
