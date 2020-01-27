from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainpage/homePage.html')

def contact(request):
    return render(request, 'mainpage/Contact.html',{'values':['Если у вас остались вопросы, то задайте их мне по телефону','8 (905) 979-10-76']})

def about(request):
    return render(request, 'mainpage/About.html')

def cabinet(request):
    return render(request, 'mainpage/Cabinet.html')

def service(request):
    return render(request, 'mainpage/Service.html')

def uslugi(request):
    return render(request, 'mainpage/Uslugi.html')
# Create your views here.
