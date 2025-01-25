from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

def home(request):
    posts = Post.objects.all()

    return render(request, 'posts/allposts.html',{'posts': posts})

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     raise Http404("Given query is not found")
    
    post = get_object_or_404(Post, pk=pk)
      
    return render(request, 'posts/post_detail.html', {'post': post})
