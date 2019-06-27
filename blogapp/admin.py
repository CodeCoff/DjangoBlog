from django.contrib import admin
from .models import Post
# Register your models here.
# here we will add our models here so that it shows in the admin page


#this means we are registering our 'Post' model to the admin
admin.site.register(Post)