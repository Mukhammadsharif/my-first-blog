# Generated by Django 3.2 on 2021-04-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_rename_category_id_books_categoryid'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='books',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
    ]
