from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #always put in request
    template_name = 'payment/templates/index.html'
    return render(request,template_name)
