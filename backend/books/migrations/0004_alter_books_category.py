# Generated by Django 3.2 on 2021-04-10 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210410_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.categories'),
        ),
    ]
