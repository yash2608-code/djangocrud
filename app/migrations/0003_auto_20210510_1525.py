# Generated by Django 2.0 on 2021-05-10 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='User',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
