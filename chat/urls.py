from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_group', views.new_group, name='new_group'),
	path('join_group/<uuid:uuid>', views.join_group, name='join_group'),
	path('leave_group/<uuid:uuid>', views.leave_group, name='leave_group'),
	path('remove_group/<uuid:uuid>', views.remove_group, name='remove_group'),
	path('open_chat/<uuid:uuid>', views.open_chat, name='open_chat'),
    # chat serializer
	path('api/chatlist/', views.GroupAPIList.as_view(), name='chatlist'),
	path('api/chats/', views.GroupCreateAPIView.as_view(), name='create_chat'),
	path('api/chats/<int:pk>/', views.GroupAPIDetailVeiw.as_view(), name='update_chat'),
    # message serializer
	path('api/messages/', views.MessageAPICreateView.as_view(), name='create_message'),
    path('api/messages/<int:pk>/', views.MessageAPIDetailVeiw.as_view(), name='update_message'),
    path('api/chats/<int:chat_id>/messages', views.MessageList.as_view(), name='message-list'),

]

urlpatterns += staticfiles_urlpatterns()
