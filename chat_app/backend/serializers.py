from django.contrib.auth.models import User
from backend.models import *
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["user", "chat_room", "message"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

class ChatRoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = ChatRoom
        fields = ["join_code", "users", "messages"]

class UserProfileSerializer(serializers.ModelSerializer):
    the_user = UserSerializer(many=True, read_only=True)
    chat_rooms = ChatRoomSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user.id')
    class Meta:
        model = UserProfile
        fields = ["the_user", "id", "user_id", "profile_image", "chat_rooms", "messages"]
