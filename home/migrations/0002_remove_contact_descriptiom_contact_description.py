# Generated by Django 4.0.2 on 2022-07-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='descriptiom',
        ),
        migrations.AddField(
            model_name='contact',
            name='Description',
            field=models.TextField(default='Default desc', max_length=500),
            preserve_default=False,
        ),
    ]
