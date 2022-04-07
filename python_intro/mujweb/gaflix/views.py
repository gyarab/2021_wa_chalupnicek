from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Movie, Category

def category_detail(request, category_id):
    context = {
        'movies': Movie.objects.filter(categories__id=category_id),
        'categories': Category.objects.all()
    }
    return render(request, 'homepage.html', context)

def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    context = {
        'movie': movie,
    }
    return render(request, 'movie_detail.html', context)

def movielist(request):
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'homepage.html', context)
