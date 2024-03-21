#serializer.py
from rest_framework import serializers
from .models import Profile, Message, UserStatus, CloudStorage, ChatRoom, MessageHistory, ChatUser, Notification, APIKey
from django.contrib.auth.models import User

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['key', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'name', 'bio', 'avatar']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'timestamp', 'content']

class UserStatusSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserStatus
        fields = ['id', 'user', 'is_online']

class CloudStorageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CloudStorage
        fields = ['id', 'user', 'message', 'profile_data']

class ChatRoomSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'participants']

class MessageHistorySerializer(serializers.ModelSerializer):
    room = ChatRoomSerializer()
    sender = UserSerializer()

    class Meta:
        model = MessageHistory
        fields = ['id', 'room', 'sender', 'timestamp', 'content']

class ChatUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ChatUser
        fields = ['id', 'user', 'is_searchable']

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Notification
        fields = ['id', 'user', 'content', 'timestamp', 'is_read']