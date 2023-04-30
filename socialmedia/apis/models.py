import uuid
from django.db import models

class tbl_users(models.Model):
    # primary users table holding all user data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    password = models.CharField(max_length=24)
    user_name = models.CharField(max_length=18)
    followers = models.PositiveSmallIntegerField(default=0)
    following = models.PositiveSmallIntegerField(default=0)

class tbl_posts(models.Model):
    # model class dealing with posts
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(tbl_users, on_delete=models.CASCADE)
    no_of_likes = models.PositiveSmallIntegerField(default=0)
    no_of_comments = models.PositiveSmallIntegerField(default=0)

class tbl_comments(models.Model):
    # model class dealing with comments
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=50)
    post = models.ForeignKey(tbl_posts, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_users, on_delete=models.CASCADE)
    
class tbl_likes(models.Model):
    # Class keeping track of likes per user
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(tbl_posts, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_users, on_delete=models.CASCADE, related_name='liked_by_user')

class tbl_follow(models.Model):
    # Model keeping track of followers/following
    id = models.AutoField(primary_key=True)
    follower_user = models.ForeignKey(tbl_users, on_delete=models.CASCADE)
    following_user = models.ForeignKey(tbl_users, on_delete=models.CASCADE, related_name='following_user')
    