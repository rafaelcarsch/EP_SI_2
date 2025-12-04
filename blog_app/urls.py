from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostEditView, PostDeleteView,
    CommentCreateView, CategoryListView, CategoryDetailView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comment/', login_required(CommentCreateView.as_view()), name='comment_form'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]