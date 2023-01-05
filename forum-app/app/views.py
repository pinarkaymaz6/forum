from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment, User
from django.utils import timezone


def index(request):
    latest_posts = Post.objects.order_by('created_at')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'forum/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, 'forum/detail.html', context)


def add_post(request):
    try:
        title = request.POST['title']
        context = request.POST['content']
        post = Post(title=title, content=context, created_at=timezone.now())
        post.save()
    except:
        return render(request, 'forum/index.html')

    return HttpResponseRedirect(reverse('forum:index'))


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    owner_id = get_object_or_404(User, pk=post.owner_id)
    try:
        comment = request.POST['comment']
        post.comment_set.create(content=comment, created_at=timezone.now(), owner_id=owner_id)
        post.save()
    except:
        return render(request, 'forum/detail.html', {'post': post, 'error_message': 'Please enter some text'})

    return HttpResponseRedirect(reverse('forum:detail', args=(post.id,)))
