from django import forms
from .models import MovieComments


class MovieCommentsForm(forms.ModelForm):
    class Meta:
        model = MovieComments
        fields = ('comment',)
