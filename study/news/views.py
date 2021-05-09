from django.shortcuts import render

def news_home(request):
    return render(request, 'firstapp/about.html')
