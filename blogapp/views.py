from django.shortcuts import render
#we will use real data from database which is why we need to import the models
from .models import Post
#this helps us with creating more feature rich views and is provided by django
from django.views.generic import (
                                ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView,
                                DeleteView)

#LoginRequiredMixin helps us prevent user access forms without loggin in
#UserPassesTestMixin helps us prevent random user make any changes in existing posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#we need to add request arg for route functions to work
def home(request):
    #this is how we get the database objects. In this case, we are getting 'Post' objects from database
    context = {
        'posts': Post.objects.all()
    }
    #render takes request as a first arg, 2nd arg is the location of the html file, 3rd arg is to make the context available in template file.
    #this still returns httpresponse behind the scene
    return render(request, 'blogapp/home.html', context)
    #this returns the html tag as a httpResponse
    #do this just for one tag. Standard method is to use templates
    #return HttpResponse('<h1>Blog Home<h1>')

#class based view. This is inheriting ListView that django provides
class PostListView(ListView):
    model = Post
    #this is to let django know that we want this specific template to be used instead of
    #the naming convention template that django looks for by default on the class views
    template_name = 'blogapp/home.html'
    #this is what we have in home.html for loop
    context_object_name = 'posts'
    #this is to order our posts from latest to oldest
    ordering = ['-date_posted']

#class based view. This is inheriting DetailView that django provides
class PostDetailView(DetailView):
    model = Post
    #for class based views, by default django looks the template in <app>/<model>_<viewtype>.html
    #so in this case, our template will be located at blogapp/post_detail.html

#class based view. This is inheriting CreateView that django provides
#LoginRequiredMixin prevents user to create a new post without logging in
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #fields we want to show when creating a new post in our site
    fields = ['title', 'content']

    def form_valid(self, form):
        #this means the form that you are trying to submit, 
        # set the author of the post to the logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

#class based view. This is inheriting UpdateView that django provides
#LoginRequiredMixin prevents user to create a new post without logging in
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    #fields we want to show when creating a new post in our site
    fields = ['title', 'content']

    def form_valid(self, form):
        #this means the form that you are trying to submit, 
        # set the author of the post to the logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blogapp/about.html', {'title': 'About'})




