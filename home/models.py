from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/',default='images/profilepic.jpg',null=True)
    bio = models.CharField(max_length=200,blank=True)