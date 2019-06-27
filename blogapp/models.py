from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#we create our models here
#this will be one of our database table
class Post(models.Model):
    #field of our table that is a character field and has a restriction of 100 character
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #on_delete=models.CASCADE means if a user is deleted, their posts will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #reverse returns a full path as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

