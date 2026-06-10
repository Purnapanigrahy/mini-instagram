from django.urls import path
from . import views

urlpatterns=[
    path('',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('home',views.home,name='home'),
    path('search',views.search,name='search'),
    path('create_post',views.create_post,name='create_post'),
    path('reels',views.reels,name='reels'),
    path('profile',views.profile,name='profile'),
    path('setting',views.setting,name='setting'),
    path('logout',views.logout_view,name='logout'),
    path('profile/<int:userid>/',views.user_profile,name='user_profile'),
]