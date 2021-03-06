# Generated by Django 3.2.6 on 2022-04-02 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('power_pet_pro_app', '0011_added_orders_app_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinions', models.TextField(max_length=500)),
                ('suggestions', models.TextField(max_length=500)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_submitted'],
            },
        ),
        migrations.CreateModel(
            name='FeedBackQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(1, 'Needs major improvements'), (2, "You could've done better"), (3, 'I think you nailed it'), (4, 'Better than I expected'), (5, 'I think you excel in this area')], default=1)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='power_pet_pro_app.feedback')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='power_pet_pro_app.feedbackquestions')),
            ],
        ),
    ]
