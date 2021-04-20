# Generated by Django 3.2 on 2021-04-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('subject', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]