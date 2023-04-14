from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

# from django import request
# Create your views here.



class TasksForm(forms.Form):
    task = forms.CharField(label="New task")
    # number = forms.IntegerField(label="Number", min_value=1, max_value=10)


def index(request):
    if request.method == "POST":
        request.session["tasks"] = []


    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "task/index.html",{
        "tasks" : request.session["tasks"]
    })

def add(request):
    # if request.method == "POST":
    #     form = TasksForm(request.POST)
    #     if form.is_valid:
    #         task = form.cleaned_data["task"]
    #         tasks.append(task)
    #     else:
    #         return render(request, "task/add.html", {
    #             "form": form 
    #         })
    if request.method == "POST":
        task = request.POST.get("task")
        request.session["tasks"] += [task]
        return HttpResponseRedirect(reverse("tasks:index"))



    return render(request, "task/add.html", {
        "form": TasksForm()
    })

