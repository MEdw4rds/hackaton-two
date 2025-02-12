# Generated by Django 4.2.18 on 2025-01-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist_profiles', '0004_alter_therapistprofile_bio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'ordering': ['day', 'start_time'], 'verbose_name_plural': 'Availability'},
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='therapistprofile',
            name='services',
            field=models.ManyToManyField(blank=True, related_name='therapists', to='therapist_profiles.service'),
        ),
    ]
