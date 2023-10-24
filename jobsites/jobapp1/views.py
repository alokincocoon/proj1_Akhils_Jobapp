import re
from django.shortcuts import redirect, render
from requests import request
from django.contrib import messages

from .models import job

def listing(request):
   job2 = job.objects.all().order_by('-id')
   return render(request,'listing.html',{"data":job2})


def new_user(request):
     if request.method == "POST":
           full_name = request.POST['fullname']
           email = request.POST['email']
           dob = request.POST['dob']
           phone_number = request.POST['phonenumber']
           gender = request.POST['gender']
           job_type = request.POST['job_type']
           experience_type = request.POST['experience_type']
           address = request.POST['address']
           city=request.POST['city']
           address2=request.POST['address2']
           pincode = request.POST['pincode']
           state = request.POST['state']
           country = request.POST['country']
           countrycode=request.POST['countrycode']
       

           def validateFullname():
               if full_name == "" or full_name is None or len(full_name) <= 3 or len(full_name) >= 30:
                  return False
               else:
                  return True

           def validatephonenumber():
                pattern = r'(^[\+0-9]{1,3})*([0-9]{10,11}$)'
                rule = re.compile(pattern)
                if phone_number is not None and phone_number != "" and rule.match(phone_number):
                  return True
                else:
                  return False

           def validateEmail():
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                rule = re.compile(pattern)
                if email is not None and email != "" and rule.match(email):
                  return True
                else:
                  return False

           def validfulladdress():
                if address == "" or state == "" or country == "" or city == "" or address2==True:
                  return False
                else:
                  return True

           def validgender():
                if gender in ["male", "Male", "female", "Female", "others", "Others"]:
                  return True
                else:
                  return False

           def validpin():
                if len(pincode) > 6 and pincode == "":
                 return False
                else:
                 return True
           def validateRole():
               if job_type in [ "Software Engineer" ,"Teacher" ,"Driver" ,"Data Analyst" ,"Cloud Engineer" ]:
                 return True
               else:
                 return False
        
          
           def validateExperience():
               if experience_type in ["0-1 years", "1-2 years",  "2-4 years" , "4-5 years" , "5+ years" ]:
                  return True
               else:
                  return False
           if validateFullname() and validatephonenumber() and validateEmail() and validfulladdress() and validgender() and validpin() and  validateExperience() and validateRole()==True:
             job2 = job.objects.create(
                  fullname=full_name, email=email, dob=dob, phonenumber=phone_number, gender=gender,
                  job_type=job_type, experience_type=experience_type, address_line1=address, pincode=pincode,
                  state=state, country=country,city=city,address_line2=address2,countrycode=countrycode
                  )
           
             job2.save()
             print(full_name,city,address2,experience_type,job_type,countrycode)
             messages.success(request,"Successfully submitted the application")
           return redirect('listing')
     return render(request,'newuser.html')
def EditTask(request):
    userid = request.GET['userid']
    userdata = job.objects.get(id=userid)
    
    if request.POST:
           full_name = request.POST['fullname']
           email = request.POST['email']
           dob = request.POST['dob']
           phone_number = request.POST['phonenumber']
           gender = request.POST['gender']
           job_type = request.POST['job_type']
           experience_type = request.POST['experience_type']
           address = request.POST['address']
           city=request.POST['city']
           address2=request.POST['address2']
           pincode = request.POST['pincode']
           state = request.POST['state']
           country = request.POST['country']
           countrycode=request.POST['countrycode']

         

           def validateFullname():
                if full_name == "" or full_name is None or len(full_name) <= 3 or len(full_name) >= 25:
                  return False
                else:
                  return True
           def validatephonenumber():
                pattern = r'(^[\+0-9]{1,3})*([0-9]{10,11}$)'
                rule = re.compile(pattern)
                if phone_number is not None and phone_number != "" and rule.match(phone_number):
                  return True
                else:
                  return False

           def validateEmail():
                pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                rule = re.compile(pattern)
                if email is not None and email != "" and rule.match(email):
                  return True
                else:
                  return False

           def validfulladdress():
                if address == "" or state == "" or country == "":
                  return False
                else:
                  return True

           def validgender():
                if gender in ["male", "Male", "female", "Female", "others", "Others"]:
                  return True
                else:
                  return False

           def validpin():
                if len(pincode) > 6 and pincode == "":
                 return False
                else:
                 return True
           def validateRole():
               if job_type in [ "Software Engineer" ,"Teacher" ,"Driver" ,"Data Analyst" ,"Cloud Engineer" ]:
                 return True
               else:
                 return False
        
          
           def validateExperience():
               if experience_type in ["0-1 years", "1-2 years",  "2-4 years" , "4-5 years" , "5+ years" ]:
                  return True
               else:
                  return False

           if validateFullname() and validatephonenumber() and validateEmail() and validfulladdress() and validgender() and validpin() and  validateExperience() and validateRole()==True:
              updated =job.objects.get(id=userid)
              updated.fullname = full_name
              updated.email=email
              updated.dob=dob
              updated.phonenumber=phone_number
              updated.gender=gender
              updated.job_type=job_type
              updated.experience_type=experience_type
              updated.address_line1=address
              updated.address_line2=address2
              updated.city=city
              updated.pincode=pincode
              updated.state=state
              updated.country=country
              updated.countrycode=countrycode 
              updated.save()
              messages.success(request,"Successfully updated the application")
              return redirect('listing')
           messages.error(request,"something went wrong")
    return render(request,'edit.html',{ "job":userdata })
def deleteData(request):
    userid=request.GET['userid']
    job.objects.get(id=userid).delete()
    return redirect('listing')