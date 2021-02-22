from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from .form import signUpForm


# Create your views here.

def signup(response):
    return render(response, "signup.html", {})

def home(request):
    return HttpResponse("HomePage")

def signin(response):
    return render(response, "signin.html", {})

def userPage(request):
    return HttpResponse("userPage")

def createAccount(request):
    return render(request,"signin.html")


def add_account(request):
    return render(request, "signin.html")