from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'websites/index.html')
    # return HttpResponse("hello,world. You are act at chai or coffe")

def home1(request):
    return HttpResponse("hello,world. You are act at chai or coffe with rutuja")

def home2(request):
    return HttpResponse("hello,world. You are act at chai or coffe")

def home3(request):
    return HttpResponse("hello,world. You are act at chai or coffe")







