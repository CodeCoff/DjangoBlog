from django.shortcuts import render, redirect
#this will help us give a flash message in our site
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    #checks if the request was a POST request and if yes, do the conditional logic
    if request.method == 'POST':
        #create a new form with the data that was in request.POST
        form = UserRegisterForm(request.POST)
        #is our form valid? (checks with our backend) if false, goest to 'else' logic
        if form.is_valid():
            #save the user. It automatically hashes the user password and save
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    #{'form':form}  means we are passing form as a context so we can access form in the template
    return render(request, 'users/register.html', {'form':form})

#login_required means login is required for the user to view this
@login_required
def profile(request):
    if request.method == 'POST':   
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
    