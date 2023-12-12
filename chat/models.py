from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()

class Group(models.Model):
	uuid = models.UUIDField(default=uuid4, editable=False)
	chatname = models.CharField(blank=False, max_length=50)
	members = models.ManyToManyField(User, blank=True, null=True)

	def __str__(self):
		return self.chatname

	def add_user(self, user):
		self.members.add(user)
		self.save()
		return

	def remove_user(self, user):
		self.members.remove(user)
		self.save()
		return


class Message(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	timestamp = models.CharField(max_length=255, blank=True, null=True)
	content = models.TextField()
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

	def __str__(self):
		return self.author.username 


class SupportMessage(models.Model):
	author_name = models.CharField(max_length=255, default="User")
	author_email = models.EmailField(max_length=50, unique=False)
	timecreate = models.DateTimeField(auto_now_add=True)
	content = models.TextField()

	def __str__(self):
		return self.author_name