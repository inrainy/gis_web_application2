from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hi_world(request):
    return render(request, 'accountapp/hi_world.html')