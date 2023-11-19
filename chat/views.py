from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .serializers import GroupSerializer, MessageSerializer
from .models import Group, Message

from rest_framework import generics


def home(request):
    groups = Group.objects.all()
    return render(request, 'home.html', {'groups': groups})


@login_required
def new_group(request):
    chatname = request.POST['chatname']
    custome_user = request.user
    if request.method == 'POST':
        new = Group.objects.create(chatname=chatname)
        new.members.add(custome_user)
        new.save()
        return redirect('home')
    else:
        messages.error(request, 'Here is error.')
        return render(request, 'home.html')


@login_required
def join_group(request, uuid):
    custome_user = request.user
    gp = Group.objects.get(uuid=uuid)
    gp.members.add(custome_user)
    gp.save()
    return redirect('home')


@login_required
def leave_group(request, uuid):
    custome_user = request.user
    gp = Group.objects.get(uuid=uuid)
    gp.members.remove(custome_user)
    gp.save()
    return redirect('home')


@login_required
def open_chat(request, uuid):
    group = Group.objects.get(uuid=uuid)
    if request.user not in group.members.all():
        return HttpResponseForbidden('Not a member. Try another group.')
    messages = group.message_set.all()
    # sorted_messages = sorted(messages, key=lambda x: x.timestamp)
    return render(request, 'chat.html', context={'messages': messages, 'uuid': uuid})


@login_required
def remove_group(request, uuid):
    # custome_user = request.user
    Group.objects.get(uuid=uuid).delete()
    return redirect('home')


class GroupAPIList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupAPIDetailVeiw(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MessageAPICreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageAPIDetailVeiw(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageList(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        # Получите ID чата из URL параметров (или из другого места, где он доступен)
        chat_id = self.kwargs['chat_id']

        # Фильтруйте сообщения по ID чата
        queryset = Message.objects.filter(group_id=chat_id)
        return queryset
