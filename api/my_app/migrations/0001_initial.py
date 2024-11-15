# Generated by Django 5.1.2 on 2024-10-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('musical_instrument', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('info', models.TextField(blank=True)),
                ('user_tg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('musical_genre', models.CharField(max_length=250)),
                ('who_need', models.CharField(max_length=250)),
                ('info', models.TextField(blank=True)),
                ('user_tg', models.IntegerField()),
            ],
        ),
    ]