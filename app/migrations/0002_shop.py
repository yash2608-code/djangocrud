# Generated by Django 2.0 on 2021-05-05 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shop_name', models.CharField(max_length=100, null=True)),
                ('Shop_type', models.CharField(max_length=100, null=True)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
