
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        #print(receipe_name)  
        #print(receipe_description)  

       
        Receipe.objects.create(
           receipe_name= receipe_name,
        receipe_description=receipe_description,

        )
        return redirect('/receipes')
    queryset=Receipe.objects.all()
    context={'receipes':queryset}

    return render(request, 'receipes.html',context)
def update_receipe(request,id):
     queryset=Receipe.objects.get(id=id)
     if request.method=="POST":
         data = request.POST
         receipe_name = data.get('receipe_name')
         receipe_description = data.get('receipe_description')
         queryset.receipe_name=receipe_name
         queryset.receipe_description=receipe_description
         queryset.save()
    
         return redirect('/receipes/')
         
     context={'receipes':queryset}

     
     return render(request, 'update_receipes.html',context)


def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    
    return redirect('/receipes/') 
def login_page(request):
    if request.method == 'POST':  # Check for POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username not found.')
            return redirect('/login/')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid password.')
            return redirect('/login/')

        
        else:
           login(request, user)
           return redirect('/receipes/')  # Correct spelling of 'recipes'

    # Handle GET requests (render the login form)
    return render(request, 'login.html') 

     
def logout_page(request):
    
    return redirect('/login/') 



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'username alerady exist')
            return redirect('/register/')

        # Ensure username is passed to the User model
        user = User.objects.create(
            username=username,
            #password=password  # Directly set the password here
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')

        return redirect('/register/')
    return render(request,'register.html')
    