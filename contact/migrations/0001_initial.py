# Generated by Django 4.2.18 on 2025-01-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('added_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
