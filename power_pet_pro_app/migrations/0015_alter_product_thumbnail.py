# Generated by Django 3.2.6 on 2022-04-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power_pet_pro_app', '0014_feedback_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='product_thumbnail/'),
        ),
    ]
