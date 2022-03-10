from django.shortcuts import render
from .models import Movie, Category

def category_detail(request, category_id):
    context = {
        'movies': Movie.objects.filter(categories__id=category_id),
        'categories': Category.objects.all()
    }
    return render(request, 'homepage.html', context)

def movielist(request):
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'homepage.html', context)
