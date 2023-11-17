from django.shortcuts import render
from django.http import HttpResponse
def hitman(request):
    return render(request,'hitman.html')
def hm(request):
    return HttpResponse('<h1>Best captain in 2023')
