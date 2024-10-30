from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student



# create yours views here
def home(request):
   return HttpResponse("Welcome to Django Training At Career Bridge")

def index(request):
    our_dict={'insert_myDjangoSecond':"welcome to the training session coming from views.py"}
    return render(request, 'myDjangoSecond_app2/index.html',context=our_dict)
# Create your views here.
def student_table(request):
    students=Student.objects.all()
    return render(request, 'myDjangoSecond_app2/student_table.html',{'students':students})