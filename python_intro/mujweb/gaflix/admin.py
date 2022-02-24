from django.contrib import admin
from .models import Movie, Actor, Director, Category

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date']
    search_fields = ['name']

admin.site.register(Movie)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director)
admin.site.register(Category)
