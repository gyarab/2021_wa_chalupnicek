from threading import active_count
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Movie, Category, Actor, SEX_MALE, SEX_FEMALE


def category_detail(request, category_id):
    try:
        context = {
            'movies': Movie.objects.filter(categories__id=category_id),
            'categories': Category.objects.all(),
            'active_category': Category.objects.get(id=category_id)
        }
    except Category.DoesNotExist:
        return HttpResponseNotFound("Category does not exist") 
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

def actorlist(request):
    context = {
        # 'actors': Actor.objects.all(),
        # 'actors': Actor.objects.filter(sex=SEX_FEMALE),
        # 'actors': Actor.objects.filter(name__icontains="m"),
        # 'actors': Actor.objects.filter(birth_date__year__gte=1963),
        'actors': Actor.objects.filter(birth_date__year__gte=1963).order_by("-birth_date"),
        'SEX_MALE': SEX_MALE,
        'SEX_FEMALE': SEX_FEMALE
    }
    return render(request, 'actors.html', context)
