from django.contrib import admin
from django.urls import path
#import views module from the same package
from . import views
from .views import (
                    PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView)


urlpatterns = [  
    #this is using a class view. We have a class named PostListView. When working with class view,
    #we need to pass in a .as_view()
    path('', PostListView.as_view(), name='blog-home'),
    #when the url goes to empty route, it handles the "home" function from 
    #views.py . "name" will help us during UI customization 
    #Naming convention for name is the appNameAndRoute eg. here blog-home
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]