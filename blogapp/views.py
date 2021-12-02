from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post,Secrets
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer,SecretsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):

    blogapp = Post.objects.all()
    paginator = Paginator(blogapp, 5)
    page = request.GET.get('page')
    blogapp = paginator.get_page(page)

    return render(request,'index.html', {'blogapp': blogapp})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def search(request):

    query=request.GET.get('q')
    result=Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    return render(request,'index.html',{'blogapp':result})

#https://djangostars.com/blog/rest-apis-django-development/
class post_list(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class post_details(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class secretlistview(ListCreateAPIView):
    serializer_class = SecretsSerializer
    queryset = Secrets.objects.all()

class secretdetailview(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = SecretsSerializer
    queryset = Secrets.objects.all()



