from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Post
from django.utils import timezone

# lista
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts': posts})

# detalhe (404 se não existe)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_app/post_detail.html', {'post': post})

# criar — sem form: pega valores via POST simples
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        post = Post.objects.create(title=title, content=content, posted_at=timezone.now())
        return redirect(post.get_absolute_url())
    return render(request, 'blog_app/post_form_noform.html')

# editar
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title', post.title)
        post.content = request.POST.get('content', post.content)
        post.save()
        return redirect(post.get_absolute_url())
    return render(request, 'blog_app/post_form_noform.html', {'post': post})

# delete com confirmação
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog_app/post_confirm_delete.html', {'post': post})
