# Generated by Django 5.1.2 on 2024-11-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_group_sample_musician_avatar_musician_sample_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='avatar',
            field=models.CharField(blank=True, default='', max_length=250),
            preserve_default=False,
        ),
    ]
