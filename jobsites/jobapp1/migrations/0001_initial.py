# Generated by Django 3.2.12 on 2023-10-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('phonenumber', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('job_type', models.CharField(choices=[('software_engineer', 'Software Engineer'), ('teacher', 'Teacher'), ('driver', 'Driver'), ('data_analyst', 'Data Analyst'), ('cloud_engineer', 'Cloud Engineer')], max_length=50)),
                ('experience_type', models.CharField(choices=[('0-1years', '0-1 years'), ('1-2years', '1-2 years'), ('2-4years', '2-4 years'), ('4-5years', '4-5 years'), ('5+years', '5+ years')], max_length=20)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
    ]
