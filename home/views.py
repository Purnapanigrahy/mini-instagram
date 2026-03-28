from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.method == 'POST':
        userormail = request.POST.get('userormail')
        password = request.POST.get('password')
        return redirect('profile')
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cnf_password = request.POST.get('cnf_password')
        email = request.POST.get('email')
        if password==cnf_password:
            user = User.objects.create_user(username=username,email=email,password=password)
        else:
            print('the password mismatch.')
        return redirect(home)
    return render(request,'signup.html')

def profile(request):
    return render(request,'profile.html')