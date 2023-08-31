from django.forms import ModelForm
from .models import Mynotes, Profile
from django.contrib.auth.models import User


class Notesform(ModelForm):
    class Meta:
        model = Mynotes
        fields = ['title', 'description']
        exclude = ['owner']
       # ordering =


