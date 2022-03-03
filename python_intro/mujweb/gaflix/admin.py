from django.contrib import admin
from .models import Movie, Actor, Director, Category

class ActorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'birth_date', 'sex']
    list_display_links = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['sex']
    list_editable = ['birth_date', 'sex']
    date_hierarchy = 'birth_date'

admin.site.register(Movie)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director)
admin.site.register(Category)
