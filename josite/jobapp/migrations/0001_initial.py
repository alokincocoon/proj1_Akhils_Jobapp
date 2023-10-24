# Generated by Django 4.2 on 2023-10-20 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField()),
                ('phonenumber', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('job_type', models.CharField(choices=[('Software Engineer', 'Software Engineer'), ('Teacher', 'Teacher'), ('Driver', 'Driver'), ('Data Analyst', 'Data Analyst'), ('Cloud Engineer', 'Cloud Engineer')], max_length=50)),
                ('experience_type', models.CharField(choices=[('0-1 years', '0-1 years'), ('1-2 years', '1-2 years'), ('2-4 years', '2-4 years'), ('4-5 years', '4-5 years'), ('5+ years', '5+ years')], max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(choices=[('+91', '+91'), ('+7', '+7')], max_length=50)),
            ],
        ),
    ]