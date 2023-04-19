from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Tasks
from .forms import ToDoForm
# Create your views here.
def index(request):
    todolist=Tasks.objects.all()
    return render(request,"tdlist/index.html",{
        'tdl':todolist
    })
def show(request,id):
    task=Tasks.objects.get(id=id)
    return render(request,"tdlist/show.html",{
        'task':task
    })
def validate(request,id):
    if request.method=='POST':
        task=Tasks.objects.get(id=id)
        task.status=True
        task.save()
        return redirect("index")
def create(request):
    if request.method == 'POST':
        form= ToDoForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            description=form.cleaned_data['description']
            deadline=form.cleaned_data['deadline']
            
            new=Tasks.objects.create(name=name,description=description,deadline=deadline)
            
            return redirect("index")
    else:
        form=ToDoForm()
    return render(request,'tdlist/create.html',{
            'form':form
        })
def delete(request,id):
    if request.method=="POST":
        task=Tasks.objects.get(id=id)
        task.delete()
    return redirect("index")