from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages 

# Create your views here.

def home(request):
    return render(request, 'home.html')
def books_page(request):
    return render(request, 'books.html')
def feedback_page(request):
    return render(request, 'feedback.html')
def about_page(request):
    return render(request, 'about.html')
def index_page(request):
    return render(request, 'index.html')
def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect homepage
            return render(request, 'index.html') 
        else:
            # Return an error message or render the login page again with an error message
            messages.error(request,"Bad Credentials" )
    
    return render(request, 'login.html')
    
def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name= request.POST['name']
        email = request.POST['email']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exists Please try another username")
            return render(request, 'signup.html')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists Please try another email")
            return render(request, 'signup.html')

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=name
        myuser.save()
        messages.success(request,"Your account has been successfully created")

        return redirect('login')




    return render(request, 'signup.html')
def question_page(request):
    return render(request, 'question_papers.html')
def profile_page(request):
    return render(request, 'profile.html')

#def signout(request):
    #logout(request)
    #messages.success(request,"Successfully logged out")
    #return redirect('home')
    



    
