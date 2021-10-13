# Generated by Django 3.2.8 on 2021-10-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basis', '0002_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
    ]
