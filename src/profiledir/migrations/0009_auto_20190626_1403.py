# Generated by Django 2.2 on 2019-06-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiledir', '0008_auto_20190626_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my location default', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
