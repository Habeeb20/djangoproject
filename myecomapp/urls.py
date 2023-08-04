from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('',PostListView.as_view(), name='app-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='goods-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='goods-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='goods-delete'),
    path('post/new/', PostCreateView.as_view(), name='goods-create'),
    path('about/', views.about, name='app-about'),
]