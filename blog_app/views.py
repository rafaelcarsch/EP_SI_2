from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment

class PostListView(ListView):
    model = Post
    template_name = "blog_app/post_list.html"
    context_object_name = "posts"
    ordering = ['-posted_at']


class PostDetailView(DetailView):
    model = Post
    template_name = "blog_app/post_detail.html"
    context_object_name = "post"

    # envia também os comentários ordenados
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(
            post=self.object
        ).order_by("-posted_at")
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog_app/post_form.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog_app/post_form.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog_app/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']  
    template_name = "blog_app/comment_form.html"
    login_url = '/login/'   # ajuste para sua URL de login

    def form_valid(self, form):
        # obtém o post da URL
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        
        form.instance.post = post
        form.instance.author = self.request.user  # usuário logado

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.kwargs["post_id"]})