# Generated by Django 5.1.2 on 2024-11-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeapp', '0005_alter_companyrecruiter_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placementsession',
            name='session_name',
            field=models.CharField(max_length=150),
        ),
    ]