#page containing the models of different data types and named JobApplicationForm
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from datetime import date
from django.db import models

def validate_fullname(value):
    if not value:
        raise ValidationError(_('Name field cannot be empty.'))
    if len(value) < 4 or len(value) > 100:
        raise ValidationError(_('Number of letters must be between 4 and 100.'))
def validate_phone_number(value):
    phone_regex = r'^\d{10}$'
    if not re.match(phone_regex, value):
        raise ValidationError(_('Invalid phone number.'))
def validate_Dob(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age < 18:
        raise ValidationError(_('You must be at least 18 years old.'))
def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError(_('Invalid email address.'))
def validate_experience_type(value):
    if value == '':
        raise ValidationError(_('Please select an option.'))
def validate_job_type(value):
    if value == '':
        raise ValidationError(_('Please select an option.'))

class JobApplicationModel(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]

    JOB_TYPE_CHOICES = [
        ('','please select an option'),
        ('Software Engineer', 'Software Engineer'),
        ('Teacher', 'Teacher'),
        ('Driver', 'Driver'),
        ('Data Analyst', 'Data Analyst'),
        ('Cloud Engineer', 'Cloud Engineer'),
    ]

    EXPERIENCE_CHOICES = [
        ('','please select an option'),
        ('0-1 years', '0-1 years'),
        ('1-2 years', '1-2 years'),
        ('2-4 years', '2-4 years'),
        ('4-5 years', '4-5 years'),
        ('5+ years', '5+ years'),
    ]

    COUNTRY_CODE_CHOICES = [
        ('+91', '+91'),
        ('+7', '+7'),
    ]

    fullname = models.CharField(max_length=100,validators=[validate_fullname])
    email = models.EmailField(max_length=100,validators=[validate_email])
    dob = models.DateField(validators=[validate_Dob])
    phonenumber = models.CharField(max_length=15,validators=[validate_phone_number])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default=None)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES,validators=[validate_job_type])
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES,default=None,validators=[validate_experience_type])
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50,blank=True, null=True)
    countrycode = models.CharField(max_length=3, choices=COUNTRY_CODE_CHOICES, default='+91', blank=True, null=True)

    def __str__(self):
        return self.fullname 
    