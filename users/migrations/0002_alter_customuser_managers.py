# Generated by Django 3.2.6 on 2021-09-25 19:34

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', users.models.UserAccountManager()),
            ],
        ),
    ]
