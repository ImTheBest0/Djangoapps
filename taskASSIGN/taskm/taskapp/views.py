from django.shortcuts import render
from django.http import HttpResponseRedirect,  Http404,HttpResponseForbidden
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from .forms import tasksForm,answerForm
from django.views.generic.edit import FormView
from rest_framework import generics
from datetime import datetime

import logging

from .models import Workers,Managers,tasks,instructions,resolutiondocs
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('taskapp:login'))
    else:
        user=request.user
        if Workers.objects.filter(user=user).exists(): 
            return render(request,"taskapp/indexworker.html",{
                'worker':Workers.objects.get(user=user)
                
            })
        if Managers.objects.filter(user=user).exists():
            return render(request,"taskapp/indexmanager.html",{
                'manager':Managers.objects.get(user=user)
            })
        else:
            return HttpResponseRedirect(reverse('taskapp:login'))
            
def login(request):
    context={}
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('taskapp:index')
        else:
            context["message"]="Incorrect Username or Password."
            return render(request,"taskapp/login.html",context)
    else:
        return render(request,"taskapp/login.html")
def logout(request):
    auth_logout(request)
    return redirect('taskapp:index')

        
class assign(FormView):
    form_class = tasksForm
    template_name = 'taskapp/assign.html'  # Replace with your template.
    success_url = reverse_lazy("taskapp:index") # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        if form.is_valid():
            
            task=form.save(commit=False)
            task.save()
            task.manager.add(Managers.objects.get(user=request.user).pk)
            task.save()
            files = request.FILES.getlist('instructions')
            workers=request.POST.getlist('workers')
            for f in files:
                
                instruction=instructions.objects.create(file=f)
                task.instructions.add(instruction)
                
            for worker in workers:
                task.workers.add(worker)
            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
def taskdetail(request,task_id):
    task=get_object_or_404(tasks,pk=task_id)
    if Managers.objects.filter(user=request.user,tasks__pk=task_id):
        return render(request,"taskapp/TaskDetail.html",{
            'task':task
        })
    else:
        raise HttpResponseForbidden("No Rights to access")
def taskdetailw(request,task_id):
    task=get_object_or_404(tasks,pk=task_id)
    if Workers.objects.filter(user=request.user,tasks__pk=task_id):
        if request.method=="POST":
            report=request.POST.get('detailsres')
            files =request.FILES.getlist('resolutiondocs')
            for file in files:
                resoldoc=resolutiondocs.objects.create(file=file)
                task.resolutiondocs.add(resoldoc)
            task.detailsres=report
            task.completness=True
            task.completion_date=datetime.now()
            task.save()
            return redirect('taskapp:index')
        else:
            return render(request,"taskapp/TaskDetailW.html",{
            'task':task,
            'form':answerForm
        })
    else:
        raise HttpResponseForbidden("No Rights to access")
def delete(request,task_id):
    task=get_object_or_404(tasks,pk=task_id)
    if Managers.objects.filter(user=request.user,tasks__pk=task_id):
        task.delete()
        return redirect('taskapp:index')
    else:
        raise HttpResponseForbidden("No relation has been proved with the task manager")
    
def confirm(request,task_id):
    task=get_object_or_404(tasks,pk=task_id)
    if Managers.objects.filter(user=request.user,tasks__pk=task_id):
        task.confirmation=True
        task.confirmation_date=datetime.now()
        task.save()
        return redirect('taskapp:index')
    else:
        raise HttpResponseForbidden("No relation has been proved with the task manager")



     