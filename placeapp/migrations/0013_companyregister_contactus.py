# Generated by Django 5.1.2 on 2024-11-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeapp', '0012_jobapplication_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, verbose_name='Company Name')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Company Website')),
                ('address', models.TextField(verbose_name='Company Address')),
                ('recruiter_name', models.CharField(max_length=100, verbose_name="Recruiter's Name")),
                ('recruiter_email', models.EmailField(max_length=254, verbose_name="Recruiter's Email")),
                ('description', models.TextField(blank=True, null=True, verbose_name='Company Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registered At')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('contact_number', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted At')),
            ],
        ),
    ]