from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, I am working!!!")

def signup(request):
    return HttpResponse("This is sign up page!!!")

def signin(request):
    return HttpResponse("This is sign in page!!!")

def signout(request):
    return HttpResponse("This is sign out page!!!")