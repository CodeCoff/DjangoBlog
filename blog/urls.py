"""
this is the url mapping file

blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#django provided views for login and logout
from django.contrib.auth import views as auth_views
#include helps us bind together the urls from individual apps
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views


urlpatterns = [
    #this is sending admin route to admin.site.urls and running the logic from there
    path('admin/', admin.site.urls),
    #when register/ send to users.views
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    #built in login/logout views from django. as_view(template_name='users/login.html') means
    # to update the template lookup location instead of django default 'registration/login.html'
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #when the user goes to blog, give the logic from blogapp.urls
    #the include function chops of the routes url and just sends the remaining string to blogapp.urls
    #here, it chops of blog/ and sends empty / to blogapp.urls
    path('', include('blogapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
