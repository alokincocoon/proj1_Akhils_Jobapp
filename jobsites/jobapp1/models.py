from django.db import models

class job(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField()
    phonenumber = models.CharField(max_length=15) 
    countrycodechoice= [ 
    ('+91', 'India'),
    ('+71', 'America'),
    ]
    countrycode=models.CharField(max_length=3,choices=countrycodechoice,default='DEFAULT VALUE', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    job_choice = [
        ('software engineer', 'Software Engineer'),
        ('teacher', 'Teacher'),
        ('driver', 'Driver'),
        ('data analyst', 'Data Analyst'),
        ('cloud engineer', 'Cloud Engineer'),
    ]
    job_type = models.CharField(max_length=50, choices=job_choice)
    experience_types = [
        ('0-1 years', '0-1 years'),
        ('1-2 years', '1-2 years'),
        ('2-4 years', '2-4 years'),
        ('4-5 years', '4-5 years'),
        ('5+ years', '5+ years'),
    ]
    experience_type = models.CharField(max_length=20, choices=experience_types)
    address_line1 = models.TextField()
    address_line2 = models.TextField(blank=True, null=True)  
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)  
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

