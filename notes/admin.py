from django.contrib import admin

# Register your models here.
from .models import Mynotes
from .models import Profile



admin.site.register(Mynotes)
admin.site.register(Profile)


