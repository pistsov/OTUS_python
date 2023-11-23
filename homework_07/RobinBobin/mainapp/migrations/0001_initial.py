# Generated by Django 4.2.7 on 2023-11-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('ccal', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('weight_initial', models.PositiveIntegerField()),
                ('weight_goal', models.PositiveIntegerField()),
                ('daily_ccal', models.PositiveIntegerField()),
            ],
        ),
    ]
