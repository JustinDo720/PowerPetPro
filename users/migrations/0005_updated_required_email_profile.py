# Generated by Django 3.2.6 on 2022-04-18 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_created_cart_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
