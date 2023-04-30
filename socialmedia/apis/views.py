from rest_framework.views import APIView
from rest_framework.response import Response

import jwt
import datetime
from apis.models import tbl_users, tbl_posts, tbl_comments, tbl_follow, tbl_likes
from apis.serializers import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer, FollowSerializer
from socialmedia.settings import SECRET_KEY
from .utils import validate_user, get_data


# Create your views here.
class AuthenticateUser(APIView):
    """
        api/authenticate/
    """
    def get_jwt(self, req):
        # json data to encode
        json_data = {
            "sender": "API",
            "message": req,
            "date": str(datetime.datetime.now())
        }
        # encode the data with SECRET_KEY and 
        # algorithm "HS256" -> Symmetric Algorithm
        encode_data = jwt.encode(payload=json_data, \
                                key=SECRET_KEY, algorithm="HS256")
        print(encode_data)
        return encode_data
    
    def post(self, request):
        print(request.data, "\n\n")
        if 'email' in request.data and 'password' in request.data:
            print(request.data['email'], request.data['password'])
            user = tbl_users.objects.filter(email=request.data['email'], password=request.data['password'])
            print(user)
            if user:
                jwt = self.get_jwt(request.data)
                print("JWT:- ", jwt)
                return Response(jwt)
            return Response("Invalid Credentials")
        return Response("Please provide valid email and password")

class UserProfile(APIView):
    """
        api/user/
    """
    def post(self, request):
        print("Inside User Profile:- ", request.data)
        if 'jwt' not in request.data:
            return Response("Please provide valid jwt token")
        print(request.data['jwt'])
        is_valid_user = validate_user(request, request.data['jwt'])
        if is_valid_user:
            data = get_data(request.data['jwt'])
            user = tbl_users.objects.get(email=data['message']['email'], password=data['message']['password'])
            print("User:- ", user)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        return Response("Invalid User")

class FollowUser(APIView):
    """
        api/follow/{id}
    """
    def post(self, request, id):
        print(request.data)
        if 'jwt' not in request.data:
            return Response("Please provide valid jwt token")
        if 'id' not in request.data:
            return Response("Please provide id of user you want to follow")
        print(request.data['jwt'])
        is_valid_user = validate_user(request, request.data['jwt'])
        if is_valid_user:
            data = get_data(request.data['jwt'])
            user = tbl_users.objects.get(email=data['message']['email'], password=data['message']['password'])
            user_to_follow = tbl_users.objects.get(id=id)
            print("User:- ", user)
            print("User to follow:- ", user_to_follow)
            data = tbl_follow(follower_user=user, following_user=user_to_follow)
            data.save()
            user.following += 1
            user.save()
            print("Saving User 1")
            user_to_follow.followers += 1
            print("Saving User 2")
            user_to_follow.save()
            print("Data saved")
            return Response("Followed")
        return Response("Invalid User")
