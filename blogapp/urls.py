from django.contrib import admin
from django.urls import path
#import views module from the same package
from . import views
from .views import (
                    PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView,
                    UserPostListView)


urlpatterns = [  
    #this is using a class view. We have a class named PostListView. When working with class view,
    #we need to pass in a .as_view()
    path('', PostListView.as_view(), name='blog-home'),
    #when the url goes to empty route, it handles the "home" function from 
    #views.py . "name" will help us during UI customization 
    #Naming convention for name is the appNameAndRoute eg. here blog-home
    path('about/', views.about, name='blog-about'),
    #template has to be user-posts.html
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    #template has to be post-detail.html
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #template has to be post-create.html
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    #template has to be post-update.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #template has to be post-delete.html
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]