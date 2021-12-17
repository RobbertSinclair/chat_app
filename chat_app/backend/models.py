import os
import random
from django.db import models
from django.contrib.auth.models import User

def generate_secure_location():
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, blank=False, null=False, on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True, null=True, upload_to="profile_imgs")

class ChatRoom(models.Model):
    users = models.ManyToManyField(UserProfile, blank=True, null=True)
    join_code = models.CharField(unique=True, blank=True, null=True, max_length=10)

    def save(self, *args, **kwargs):
        random_selection = "1234567890ABCDEFGHIJKLMONPQRSTUVWXYZ"
        if self.join_code is None:
            new_join = ""
            for i in range(8):
                character = random.choice(random_selection)
                new_join += character
            self.join_code = new_join
        super(ChatRoom, self).save(*args, **kwargs)

class Message(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, blank=True, null=True, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)