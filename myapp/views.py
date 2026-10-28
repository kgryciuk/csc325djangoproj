from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Hello, World! This is the home page.</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page.</p>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1><p>This is the contact page.</p>")
