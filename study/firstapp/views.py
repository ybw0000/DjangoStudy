from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'Hello', '123'],
        'obj' : {
            'car' : 'bmw',
            'age' : '18',
            'hobby' : 'volleyball'
        }
    }
    return render(request, 'firstapp/index.html', data)

def about(request):
    return render(request, 'firstapp/about.html')


