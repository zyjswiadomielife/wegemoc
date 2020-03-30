from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from comments.forms import CommentFormPost
from comments.models import CommentPost
from .models import Post

def postlist(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html',
                {'posts': posts})

def postdetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created_at')[:2]

    comments = post.postcomments.all()

    if request.method =='POST':
        form = CommentFormPost(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentFormPost()
    return render(request, 'posts/detail.html',
                {'post': post,
                'similar_posts': similar_posts,
                'comments': comments,
                'form': form})