from django import forms
from movieapp.models import MovieForm
class Movie(forms.ModelForm):
    class Meta:
        model=MovieForm
        fields='__all__'
