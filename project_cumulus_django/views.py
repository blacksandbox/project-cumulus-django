from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'welcome_msg': "This is the homepage"}
    return render(request, "proj/home.html", context) 
    # return HttpResponse("Welcome")