from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. A request handler

def say_hello(request):
 return render(request, 'hello.html',{'name': 'Joy'})

def big_back(request):
    return HttpResponse('This is a Reminder')