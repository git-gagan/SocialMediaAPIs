from django.urls import path, include

from .views import AuthenticateUser, UserProfile, FollowUser

urlpatterns = [
    # path("", include('apis.urls'))
    path("authenticate/", AuthenticateUser.as_view(), name="get-token"),
    path("user/", UserProfile.as_view(), name="get-user"),
    path("follow/<str:id>", FollowUser.as_view(), name="get-user")
]