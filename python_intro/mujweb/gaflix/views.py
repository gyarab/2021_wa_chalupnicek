from django.shortcuts import render
from .models import Movie

def movielist(request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'homepage.html', context)