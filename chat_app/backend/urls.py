from django.urls import path
from backend.views import *

urlpatterns = [
    path("user/", user_list),
    path("user/<int:pk>", user_detail),
    path("user_profile/", UserProfileViewSet.as_view()),
    path("chat_room/", ChatRoomViewSet.as_view()),
    path("message/", MessageViewSet.as_view())
]