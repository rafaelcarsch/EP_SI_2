from django.urls import path
from . import views

#urlpatterns = [
#    path('about/', views.about, name='about'), # adicione esta linha
#    path('', views.index, name='index'),
#]

urlpatterns = [
    # placeholders — cada versão terá suas próprias views com os mesmos nomes
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]