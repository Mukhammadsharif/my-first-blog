# Generated by Django 3.2 on 2021-04-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210418_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
