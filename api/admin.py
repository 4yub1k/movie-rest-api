from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
  list_display = ('id', 'Title')
  list_display_links = ('id', 'Title')

  #use only for extra funxtions in admin panel, ONLY ADD MODEL FIELD NAMES TO THESE TUPLES (,)
  #list_filter = ('Title',)
  #list_editable = ('is_published',)
  #search_fields = ('Title', 'field', 'field', 'field', 'field', 'field', 'field')
  #list_per_page = 25

admin.site.register(Movie, MovieAdmin)