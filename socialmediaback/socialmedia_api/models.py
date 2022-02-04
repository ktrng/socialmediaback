from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    # images = models.ImageField(upload_to='images/')
    ##will work on this later (https://www.geeksforgeeks.org/python-uploading-images-in-django/)##

    # not sure if this will work tbh, will try and find out
    friends = models.ForeignKey('self', on_delete=models.CASCADE)

    posts = models.OneToManyField(Post, on_delete=models.CASCADE)

class Post(models.Model):
    id = models.BigAutoField()
    author = models.ForeignKey(User)
    body = models.CharField(max_length=640)
    comments = models.OneToManyField(Comment, on_delete=models.CASCADE)
    likes = models.IntegerField()

class Comment(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=640)
    likes = models.IntegerField()
