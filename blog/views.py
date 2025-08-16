from django.shortcuts import render,get_object_or_404
from .models import Post
from rest_framework import generics
from rest_framework import viewsets
from .serializers import PostSerializer # type: ignore
# Create your views here.
def post_list(request):
    posts=Post.objects.all().order_by('-created_at')
    return render(request,'blog/post_list.html',{'posts':posts})
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

class PostListAPIView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializer
#viewsets.ModelViewSet is a class that automatically provides a default implementation for create, retrieve, update, partial_update, and destroy actions for our model.
# We simply need to define the queryset (what data to get) and the serializer_class (how to format it), and DRF handles the rest.    