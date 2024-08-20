from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=255, default="Unknown Company")
    application_link = models.URLField()
    posted_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class AssistanceOption(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    cv = models.FileField(upload_to='cvs/', blank=True)

    def __str__(self):
        return self.user.username
