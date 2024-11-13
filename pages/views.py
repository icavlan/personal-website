from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse('Anasayfa')

def about_page_view(request):
    context = {
        'name': 'Ismail Çavlan', 
        'age':'47',
               }
    return render(request, 'pages/about.html', context)
