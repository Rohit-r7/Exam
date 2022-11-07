from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'index.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def academic(request):
    return render (request,'academic.html')

def student(request):
    return render (request,'student.html')
