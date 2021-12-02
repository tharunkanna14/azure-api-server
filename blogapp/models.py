from django.db import models
from django.conf import settings

from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        ordering = ['-published_date',]

def publish(self):
	self.published_date = timezone.now()
	self.save()



def __str__(self):
	return self.title

class Secrets(models.Model):
    user = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.email


