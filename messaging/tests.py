from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Message, UserStatus, CloudStorage, ChatRoom, MessageHistory, ChatUser, Notification

class ProfileModelTestCase(TestCase):
    def test_profile_creation(self):
        user = User.objects.create(username='test_user')
        profile = Profile.objects.create(user=user, name='Test Name')
        self.assertEqual(profile.user, user)
        self.assertEqual(profile.name, 'Test Name')

class MessageModelTestCase(TestCase):
    def test_message_creation(self):
        sender = User.objects.create(username='sender')
        receiver = User.objects.create(username='receiver')
        message = Message.objects.create(sender=sender, receiver=receiver, content='Test message')
        self.assertEqual(message.sender, sender)
        self.assertEqual(message.receiver, receiver)
        self.assertEqual(message.content, 'Test message')

class UserStatusModelTestCase(TestCase):
    def test_user_status_creation(self):
        user = User.objects.create(username='test_user')
        user_status = UserStatus.objects.create(user=user, is_online=True)
        self.assertEqual(user_status.user, user)
        self.assertTrue(user_status.is_online)

class CloudStorageModelTestCase(TestCase):
    def test_cloud_storage_creation(self):
        user = User.objects.create(username='test_user')
        cloud_storage = CloudStorage.objects.create(user=user)
        self.assertEqual(cloud_storage.user, user)

class ChatRoomModelTestCase(TestCase):
    def test_chat_room_creation(self):
        chat_room = ChatRoom.objects.create(name='Test Room')
        self.assertEqual(chat_room.name, 'Test Room')

class MessageHistoryModelTestCase(TestCase):
    def test_message_history_creation(self):
        sender = User.objects.create(username='sender')
        chat_room = ChatRoom.objects.create(name='Test Room')
        message_history = MessageHistory.objects.create(room=chat_room, sender=sender, content='Test message')
        self.assertEqual(message_history.room, chat_room)
        self.assertEqual(message_history.sender, sender)
        self.assertEqual(message_history.content, 'Test message')

class ChatUserModelTestCase(TestCase):
    def test_chat_user_creation(self):
        user = User.objects.create(username='test_user')
        chat_user = ChatUser.objects.create(user=user)
        self.assertEqual(chat_user.user, user)

class NotificationModelTestCase(TestCase):
    def test_notification_creation(self):
        user = User.objects.create(username='test_user')
        notification = Notification.objects.create(user=user, content='Test notification')
        self.assertEqual(notification.user, user)
        self.assertEqual(notification.content, 'Test notification')