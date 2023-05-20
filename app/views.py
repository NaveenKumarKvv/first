from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def srujana(request):
    return HttpResponse('<marquee><b><h1>thinnava ra chi po ra</h1></b></marquee>')

def meghana(request):
    return HttpResponse('<h1>hai hello how r u</h1>')