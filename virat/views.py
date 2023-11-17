from django.shortcuts import render

from django.http import HttpResponse
def viratk(request):
    return render(request,'viratk.html')
def kohli(request):
    return HttpResponse('<h1>King kohli</h1>')
