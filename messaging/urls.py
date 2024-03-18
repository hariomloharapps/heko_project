from django.urls import path
from django.views.generic import TemplateView
from .views import register, user_login, profile, send_message, inbox, search_user, messages, fetch_notifications
from .views import ProfileListAPIView, ProfileDetailAPIView, MessageListCreate, MessageDetail, UserStatusListCreate, UserStatusDetail
from .views import CloudStorageListCreate, CloudStorageDetail, ChatRoomListCreate, ChatRoomDetail, MessageHistoryListCreate, MessageHistoryDetail
from .views import ChatUserListCreate, ChatUserDetail, NotificationListCreate, NotificationDetail

from django.urls import path
from .views import GenerateAPIKey, AuthenticateWithAPIKey, AuthorizeAPIRequest







urlpatterns = [
    # Web application views
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('send-message/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
    path('search-user/', search_user, name='search_user'),
    path('messages/<str:receiver_username>/', messages, name='messages'),
    path('fetch-notifications/', fetch_notifications, name='fetch_notifications'),
    path('custom-register/', TemplateView.as_view(template_name='registration/register.html'), name='custom_register'),
    
    # API endpoints
    path('api/profiles/', ProfileListAPIView.as_view(), name='api-profile-list'),
    path('api/profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='api-profile-detail'),
    path('api/messages/', MessageListCreate.as_view(), name='api-message-list'),
    path('api/messages/<int:pk>/', MessageDetail.as_view(), name='api-message-detail'),
    path('api/user-status/', UserStatusListCreate.as_view(), name='api-user-status-list'),
    path('api/user-status/<int:pk>/', UserStatusDetail.as_view(), name='api-user-status-detail'),
    path('api/cloud-storage/', CloudStorageListCreate.as_view(), name='api-cloud-storage-list'),
    path('api/cloud-storage/<int:pk>/', CloudStorageDetail.as_view(), name='api-cloud-storage-detail'),
    path('api/chat-rooms/', ChatRoomListCreate.as_view(), name='api-chat-room-list'),
    path('api/chat-rooms/<int:pk>/', ChatRoomDetail.as_view(), name='api-chat-room-detail'),
    path('api/message-history/', MessageHistoryListCreate.as_view(), name='api-message-history-list'),
    path('api/message-history/<int:pk>/', MessageHistoryDetail.as_view(), name='api-message-history-detail'),
    path('api/chat-users/', ChatUserListCreate.as_view(), name='api-chat-user-list'),
    path('api/chat-users/<int:pk>/', ChatUserDetail.as_view(), name='api-chat-user-detail'),
    path('api/notifications/', NotificationListCreate.as_view(), name='api-notification-list'),
    path('api/notifications/<int:pk>/', NotificationDetail.as_view(), name='api-notification-detail'),
    path('generate-api-key/', GenerateAPIKey.as_view(), name='generate_api_key'),
    path('authenticate-with-api-key/', AuthenticateWithAPIKey.as_view(), name='authenticate_with_api_key'),
    path('authorize-api-request/', AuthorizeAPIRequest.as_view(), name='authorize_api_request'),
]





