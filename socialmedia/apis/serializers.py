from apis.models import tbl_users, tbl_posts, tbl_comments, tbl_follow, tbl_likes
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_users
        fields = ['user_name', 'followers', 'following']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_posts
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_comments
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_likes
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_follow
        fields = '__all__'