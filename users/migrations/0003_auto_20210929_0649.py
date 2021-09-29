# Generated by Django 3.2.6 on 2021-09-29 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('city', models.TextField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('country', models.TextField(blank=True, max_length=75, null=True)),
                ('state', models.TextField(blank=True, max_length=75, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
