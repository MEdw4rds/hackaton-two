# Generated by Django 4.2.18 on 2025-01-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist_profiles', '0002_remove_therapistprofile_availability_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='credentials',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.RemoveField(
            model_name='therapistprofile',
            name='services',
        ),
        migrations.AddField(
            model_name='therapistprofile',
            name='services',
            field=models.ManyToManyField(blank=True, to='therapist_profiles.service'),
        ),
    ]
