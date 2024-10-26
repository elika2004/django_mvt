from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h2>hello<h2>')

def contact(request):
    return HttpResponse('contact us')

def about(request):
    return HttpResponse('about us')