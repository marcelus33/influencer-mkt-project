# Generated by Django 5.0.7 on 2024-07-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('rating', models.DecimalField(decimal_places=15, max_digits=17)),
                ('platform', models.PositiveSmallIntegerField(choices=[(1, 'Instagram'), (2, 'TikTok'), (3, 'User Generated Content')])),
            ],
        ),
    ]
