from rest_framework import serializers
from .models import Post,Secrets



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class SecretsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secrets
        fields = '__all__'