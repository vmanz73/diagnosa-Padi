from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def user(request):
    return HttpResponse("<h1>test</h1>")
