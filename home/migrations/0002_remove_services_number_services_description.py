# Generated by Django 4.2.6 on 2023-10-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='number',
        ),
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
