#models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")  
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username}"

class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Online' if self.is_online else 'Offline'}"

class CloudStorage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.FileField(upload_to='messages/', blank=True)#
    profile_data = models.FileField(upload_to='profiles/', blank=True)

    def __str__(self):
        return f"CloudStorage for {self.user.username}"

class ChatRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    participants = models.ManyToManyField(User, related_name='chatrooms')

    def __str__(self):
        return self.name

class MessageHistory(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.sender.username} in {self.room.name}"

class ChatUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='chatuser')
    is_searchable = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}: {self.content}"

class APIKey(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"API Key for {self.user.username}"