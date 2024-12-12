# Generated by Django 5.1.2 on 2024-11-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeapp', '0010_jobapplication_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='contacted',
            field=models.BooleanField(default=False, help_text='Has the applicant been contacted?'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='shortlisted',
            field=models.BooleanField(default=False, help_text='Has the applicant been shortlisted?'),
        ),
    ]