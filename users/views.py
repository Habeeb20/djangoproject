from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(requesr, f'your account has been created for {username}')
            if username.is_valid():
                form.save()
                
                return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.Post, request,FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            P_form.save()
            messages.success(request, "your account has been updated")
            return redirect('Home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html')
    
    