from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.


def home(request):
    # return HttpResponse("This is the home Page.")

    context = {'name': "Rushi", 'course': "Python Django"}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        contacts = Contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
        print("Data inserted into db successfully.")


    return render(request, 'contact.html')
