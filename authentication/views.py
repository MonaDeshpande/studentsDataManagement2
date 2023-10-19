from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import students

# Create your views here.
def home(request):
    #return HttpResponse("I am working")
    return render(request, "authentication/home.html", {})

def add_student(request):
    if request.method == "POST":
        print("Data is coming")

    #Steps to fetch data
        
    #Data fetch
        student_first_name=request.POST.get("emp_name")
        student_last_name=request.POST.get("emp_name")
        student_address=request.POST.get("emp_name")
        student_mobile=request.POST.get("emp_name")
        student_Phy=request.POST.get("emp_name")
        student_Chem=request.POST.get("emp_name")
        student_Bio=request.POST.get("emp_name")
        student_Maths=request.POST.get("emp_name")

    #Create model object and set the data
        s= students()
        s.students_first_name =student_first_name
        s.students_last_name=student_last_name
        s.students_address=student_address
        s.students_phy=student_Phy
        s.students_chem=student_Chem
        s.students_bio=student_Bio
    
    #save the data
        s.save()
    



        return redirect("home")
    return render(request, "authentication/add_student.html", {})

def signup(request):
    #print("processing signup")
     return render(request, "authentication/signup.html")

def signin(request):
    #print("processing")
    return render(request, "authentication/signin.html")

def signout(request):
    pass