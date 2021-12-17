from django.contrib.auth.models import User
from backend.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class UserProfileSerializer(serializers.ModelSerializer):
    the_user = UserSerializer(many=True, read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user.id')
    class Meta:
        model = UserProfile
        fields = ["user_id", "profile_image", "the_user"]