from django import forms
from .models import JobApplicationModel
#Page containing the ModelForm
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplicationModel
        fields = '__all__'
        widgets = {
            'countrycode': forms.Select(
                attrs={'class': 'countrycode'}),
            'fullname': forms.TextInput(
               attrs={'placeholder': 'please enter the full name',"class":"input-box"}),
            'email': forms.EmailInput(
               attrs={'placeholder': 'please enter the email'}),
            'dob': forms.DateInput(
                attrs={'placeholder': 'please enter the date of birth', 'type': 'date'}),
            'phonenumber': forms.TextInput(
                attrs={'placeholder': 'please enter the phone number'}),
            'gender': forms.RadioSelect(),
            'job_type': forms.Select(
                attrs={'placeholder': 'Select a job type', 'class': 'experience'}),
            'experience_type': forms.Select(
                attrs={'class': 'experience'}),
            'address': forms.TextInput(
                attrs={'placeholder': 'please enter the address'}),
            'address2': forms.TextInput(
                attrs={'placeholder': 'please enter the address'}),
            'city': forms.TextInput(
                attrs={'placeholder': 'please enter the city'}),
            'pincode': forms.TextInput(
                attrs={'placeholder': 'please enter the pincode'}),
            'state': forms.TextInput(
                attrs={'placeholder': 'please enter the state'}),
            'country': forms.TextInput(
                attrs={'placeholder': 'please enter the country'}),
        }
