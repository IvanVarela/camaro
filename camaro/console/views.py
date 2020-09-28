from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "console/index.html")


def register(request):
    return render(request, "console/register.html")

