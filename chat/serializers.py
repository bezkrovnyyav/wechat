from rest_framework import serializers

from .models import Group, Message, SupportMessage


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','uuid', 'chatname', 'members']


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # display author name
    author_id = serializers.IntegerField()  # display author id

    class Meta:
        model = Message
        fields = ['author', 'author_id', 'timestamp', 'content', 'group']


class SupportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportMessage
        fields = ['id', 'author_name', 'author_email', 'timecreate', 'content']