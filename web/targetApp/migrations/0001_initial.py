# Generated by Django 3.2.4 on 2021-10-13 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, unique=True)),
                ('h1_team_handle', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('insert_date', models.DateTimeField()),
                ('start_scan_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('insert_date', models.DateTimeField()),
                ('domains', models.ManyToManyField(related_name='domains', to='targetApp.Domain')),
            ],
        ),
    ]
