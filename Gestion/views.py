from http.client import NOT_FOUND
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gestion(request):

    return render(request, "Gestion/gestion.html")

