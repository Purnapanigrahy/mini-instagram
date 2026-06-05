from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    if request.method == 'POST':
        userormail = request.POST.get('userormail')
        password = request.POST.get('password')
        user  = authenticate(request,username=userormail,password = password)
        if user:
            login(request,user)
            return redirect('profile')
        else:
            error = "incorrect username or password"
            return render(request,'home.html',{"error":error})
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cnf_password = request.POST.get('cnf_password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            error = 'the user alreadey existed.'
            context = {'error':error}
            return render(request,'signup.html',context)
        if password==cnf_password:
            user = User.objects.create_user(username=username,email=email,password=password)
        else:
            error = 'the password mismatch.'
            context = {'error':error}
            return render(request,'signup.html',context)
        return redirect(home)
    return render(request,'signup.html')

def profile(request):
    return render(request,'profile.html')

def edit_profile(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        bio = request.POST.get('bio')
        request.user.profile.profile_pic = profile_pic
        request.user.profile.bio = bio
        request.user.profile.save()
        
        return redirect('profile')
    return render(request,'edit_profile.html')