from django.contrib import admin
from movieapp.models import MovieForm

class Movieadmin(admin.ModelAdmin):
    list_display=['mname','heroname','heroinname','directorname','rating']

# Register your models here.
admin.site.register(MovieForm,Movieadmin)
