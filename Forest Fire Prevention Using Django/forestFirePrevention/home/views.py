from django.shortcuts import render
import templates

# Create your views here.

def home(request):
    return render(request, 'base.html')


def predict(request):
    return render(request, 'predictions.html')