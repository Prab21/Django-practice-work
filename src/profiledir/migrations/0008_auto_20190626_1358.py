# Generated by Django 2.2 on 2019-06-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiledir', '0007_auto_20190626_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='This is default text given by purushottam for testing purpose.'),
        ),
    ]