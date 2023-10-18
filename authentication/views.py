from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("I am working")
    return render(request, "authentication/home.html", {})

def signup(request):
    #print("processing signup")
    return render(request, "authentication/signup.html")

def signin(request):
    #print("processing")
    return render(request, "authentication/signin.html")

def signout(request):
    pass