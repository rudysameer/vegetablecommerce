# Generated by Django 4.2.6 on 2023-11-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('star', models.IntegerField()),
                ('review', models.TextField()),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
