# Generated by Django 3.2.8 on 2021-10-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basis', '0019_auto_20211019_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscribed_for_mailings',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='subscription_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
