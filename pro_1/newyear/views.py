from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
now = datetime.now()

# Create your views here.

def index(request):
    
    return render(request, "newyear/index.html", {
        "answer" :  random.choice(["True", "False"])
    })