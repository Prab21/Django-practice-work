# Generated by Django 2.2 on 2019-06-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiledir', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
