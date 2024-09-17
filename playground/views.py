from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from  hellokitty.forms import CreateNewList
from django.contrib.auth.decorators import login_required
# Create your views here. A request handler

@login_required
def say_hello(request):
 return render(request, 'hello.html',{'name': request.user.username})

def big_back(request):
    return HttpResponse('This is a Reminder')

def create(request):
   if request.method == 'POST':
        form=CreateNewList(request.POST)
        if form.is_valid():
           n=form.cleaned_data['name']
           n.save()
        
        return HttpResponseRedirect('/%i'%n.id)
           
   else:
      form=CreateNewList()
   return render(request,'create.html',{'form':form})