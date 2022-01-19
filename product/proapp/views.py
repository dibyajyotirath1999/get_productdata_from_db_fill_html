from django.shortcuts import render
from proapp.models import *

def product(request):
    product=prodb.objects.all()
    return render (request,"pro.html",{"product":product})
