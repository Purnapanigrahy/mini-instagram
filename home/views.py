from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from .models import Post,Reel

# Create your views here.
def signin(request):
    if request.method == 'POST':
        userormail = request.POST.get('userormail')
        password = request.POST.get('password')
        user  = authenticate(request,username=userormail,password = password)
        if user:
            login(request,user)
            return redirect('profile')
        else:
            error = "incorrect username or password"
            return render(request,'signin.html',{"error":error})
    return render(request,'signin.html')

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
        return redirect(signin)
    return render(request,'signup.html')

def profile(request):
    posts = Post.objects.filter(user=request.user)
    post_count = posts.count()
    context = {"posts": posts,"post_count":post_count}
    return render(request,'profile.html',context)

def edit_profile(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        bio = request.POST.get('bio')
        request.user.profile.profile_pic = profile_pic
        request.user.profile.bio = bio
        request.user.profile.save()
        
        return redirect('profile')
    return render(request,'edit_profile.html')

def home(request):
    posts = Post.objects.all().exclude(user=request.user).order_by('?')
    return render(request,"home.html",{"posts":posts})

def search(request):
    return render(request,"search.html")


def user_profile(request,userid):
    user = User.objects.get(id=userid)
    posts = Post.objects.filter(user=user)
    post_count = posts.count()
    context = {'user':user,'posts':posts,"post_count":post_count}
    return render(request,"user_profile.html",context)

def create_post(request):
    if request.method == 'POST':
        post = request.FILES.get('post')
        caption = request.POST.get('caption')

        Post.objects.create(
            user=request.user,
            image=post,
            caption=caption
        )
        return redirect(profile)
    return render(request,"create_post.html")

def deletepost(request,postid):
    posts = Post.objects.filter(user=request.user)
    Post.objects.get(id = postid).delete()
    return render(request,'profile.html',{"posts": posts})

def reels(request):
    return None

def setting(request):
    return render(request, "settings.html")

def logout_view(request):
    auth_logout(request)
    return redirect('signin')
    