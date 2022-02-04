from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    # images = models.ImageField(upload_to='images/')
    ##will work on this later (https://www.geeksforgeeks.org/python-uploading-images-in-django/)##

    # not sure if this will work tbh, will try and find out
    friends = models.ManyToManyField('self')

    posts = models.ForeignKey('Post', on_delete=models.CASCADE)

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    body = models.CharField(max_length=640)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)
    likes = models.IntegerField()

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    author = models.OneToOneField('User', on_delete=models.CASCADE)
    postedto = models.ForeignKey('Post', on_delete=models.CASCADE)
    body = models.CharField(max_length=640)
    likes = models.IntegerField()
