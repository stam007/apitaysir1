# Generated by Django 2.2.5 on 2019-09-09 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0024_auto_20190909_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciverequest',
            name='id_User_Giver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ReciveRequest.id_User_Giver+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reciverequest',
            name='id_User_Reciver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ReciveRequest.id_User_Reciver+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reciverequest',
            name='id_User_Sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ReciveRequest.id_User_Sender+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reciverequest',
            name='id_User_Taken',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ReciveRequest.id_User_Taken+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sendrequest',
            name='id_User_Reciver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SendRequest.id_User_Reciver+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sendrequest',
            name='id_User_Sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='SendRequest.id_User_Sender+', to=settings.AUTH_USER_MODEL),
        ),
    ]
