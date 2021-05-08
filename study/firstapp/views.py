from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4> tratasdsad <h4>")

def about(request):
    return HttpResponse("<h4> About as <h4>")