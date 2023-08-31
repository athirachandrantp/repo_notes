import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Mynotes(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    notes_image = models.ImageField(null=True, blank=True,
                    upload_to='images/', default='images/aman.jpeg')
    notes_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200, blank=True, null=True)
    notes_email = models.EmailField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.id)

