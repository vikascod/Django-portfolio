from django.shortcuts import render, HttpResponse
from home.models import Customer, Problem

# Create your views here.  vikas1@#$
def index(request):
    return render(request, 'index.html')

def about(request):
    if request.method == "POST":
        question = request.POST['question']
        feedback = request.POST['feedback']
        print(question, feedback)

        complain = Problem(question=question, feedback=feedback)
        complain.save()
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name, phone, email, desc)

        rea = Customer(name=name, phone=phone, email=email, desc=desc)
        rea.save()
    return render(request, 'contact.html')

