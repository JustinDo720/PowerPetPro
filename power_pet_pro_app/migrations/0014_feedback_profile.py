# Generated by Django 3.2.6 on 2022-04-07 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_created_cart_model'),
        ('power_pet_pro_app', '0013_updated_feedbackanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]