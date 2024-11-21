from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm

from Account.forms import Register_User_Form


# <------------------------------------------> Registrattion Form Logic <----------------------------------------->
def Register_User_View(request):
    register_form = Register_User_Form
    if request.method =='POST':
        register_form = Register_User_Form(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,'Your account has been registered successfully😉...')
            return redirect('login_user')
        else:
            messages.error(request, 'Some error occured😫...Please try again...')
            return redirect('register_user')
    else:
        return render(request, 'Account/register_user.html', {'register_form':register_form})



# <----------------------------------------------> Login Form Logic <---------------------------------------------->
def Login_User_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: # if user is there
            login(request, user) # keep him logged in
            messages.success(request, "You have been logged in successfuly...")
            return redirect('store_index_user') # url from Store app
        else:
            messages.error(request, "Please enter correct username and password...")
            return redirect('login_user')
    else:
        return render(request, 'Account/login_user.html',{})
    

# <----------------------------------------------> Login Form Logic <---------------------------------------------->
def Logout_User_View(request):
    logout(request)
    messages.warning(request, " You have been logout... ")
    return redirect('login_user')
    
