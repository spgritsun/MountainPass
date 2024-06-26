# Generated by Django 5.0.6 on 2024-06-21 23:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=100, null=True)),
                ('data1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title2', models.CharField(blank=True, max_length=100, null=True)),
                ('data2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title3', models.CharField(blank=True, max_length=100, null=True)),
                ('data3', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, max_length=50, null=True)),
                ('summer', models.CharField(blank=True, max_length=50, null=True)),
                ('autumn', models.CharField(blank=True, max_length=50, null=True)),
                ('spring', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fam', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('otc', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('other_titles', models.CharField(blank=True, max_length=100, null=True)),
                ('connect', models.CharField(blank=True, max_length=10, null=True)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coordinates')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.image')),
                ('levels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.level')),
                ('statuses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
