from django.shortcuts import render, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Profile, Message, Notification
from .forms import UserRegistrationForm
from rest_framework import generics
from .serializers import ProfileSerializer, MessageSerializer, UserStatusSerializer, CloudStorageSerializer, ChatRoomSerializer, MessageHistorySerializer, ChatUserSerializer, NotificationSerializer
from django.contrib.auth.models import User
from .models import UserStatus
from .models import CloudStorage , ChatRoom ,MessageHistory , Notification 
from django.shortcuts import render, redirect
from .models import ChatUser

# Regular views for web application
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('login')
            
            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile.objects.create(user=user, name=name)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
    
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'registration/login.html')

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_username = request.POST['receiver_username']
        content = request.POST['content']
        sender = request.user
        receiver = User.objects.get(username=receiver_username)
        message = Message.objects.create(sender=sender, receiver=receiver, content=content)
        return redirect('inbox')
    else:
        return render(request, 'send_message.html')

@login_required
def inbox(request):
    user = request.user
    received_messages = Message.objects.filter(receiver=user)
    sent_messages = Message.objects.filter(sender=user)
    return render(request, 'inbox.html', {'received_messages': received_messages, 'sent_messages': sent_messages})

@login_required
def search_user(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            users = User.objects.filter(Q(username__icontains=query))
            return render(request, 'search_user.html', {'users': users, 'query': query})
    return render(request, 'search_user.html')

@login_required
def messages(request, receiver_username):
    try:
        receiver = User.objects.get(username=receiver_username)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    messages = Message.objects.filter(sender=request.user, receiver=receiver) | \
               Message.objects.filter(sender=receiver, receiver=request.user)

    if request.method == 'POST':
        content = request.POST['content']
        sender = request.user
        receiver = User.objects.get(username=receiver_username)
        message = Message.objects.create(sender=sender, receiver=receiver, content=content)
        return redirect('messages', receiver_username=receiver_username)

    return render(request, 'messages.html', {'messages': messages, 'receiver_username': receiver_username})

@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'notifications.html', {'notifications': notifications})

# API views
class ProfileListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserStatusListCreate(generics.ListCreateAPIView):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer

class UserStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer

class CloudStorageListCreate(generics.ListCreateAPIView):
    queryset = CloudStorage.objects.all()
    serializer_class = CloudStorageSerializer

class CloudStorageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CloudStorage.objects.all()
    serializer_class = CloudStorageSerializer

class ChatRoomListCreate(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class ChatRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageHistoryListCreate(generics.ListCreateAPIView):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer

class MessageHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer

class ChatUserListCreate(generics.ListCreateAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserSerializer

class ChatUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatUser.objects.all()
    serializer_class = ChatUserSerializer

class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Profile, Message, UserStatus, CloudStorage, ChatRoom, MessageHistory, ChatUser, Notification
from .serializers import ProfileSerializer, MessageSerializer, UserStatusSerializer, CloudStorageSerializer, ChatRoomSerializer, MessageHistorySerializer, ChatUserSerializer, NotificationSerializer
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import APIKey
from .serializers import APIKeySerializer

class GenerateAPIKey(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Generate a new API key for the authenticated user
        api_key = APIKey.objects.create(user=request.user)
        serializer = APIKeySerializer(api_key)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AuthenticateWithAPIKey(APIView):
    def post(self, request, format=None):
        # Authenticate user using API key
        api_key = request.data.get('api_key')
        try:
            api_key_obj = APIKey.objects.get(key=api_key)
            user = api_key_obj.user
            return Response({'username': user.username}, status=status.HTTP_200_OK)
        except APIKey.DoesNotExist:
            return Response({'error': 'Invalid API key'}, status=status.HTTP_401_UNAUTHORIZED)

class AuthorizeAPIRequest(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Authorize API request based on API key
        # Add your authorization logic here
        return Response({'message': 'Authorized'}, status=status.HTTP_200_OK)