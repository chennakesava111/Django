# Generated by Django 3.2.7 on 2021-09-30 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=225),
            preserve_default=False,
        ),
    ]
