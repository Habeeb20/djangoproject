from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Ecommerce


def home(request):
    return render(request, "app/home.html", )


class PostListView(ListView):
    model = Ecommerce
    template_name = 'app/home.html'
    context_object_name='apps'
    ordering = ['-date_posted']
    paginate_by = 2
    
    
class  UserPostListView(ListView):
    model = Ecommerce
    template_name = 'app/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Ecommerce.Objects.filter(author=user).orderpc_by('-date_posted')

class PostDetailView(DetailView):
    model = Ecommerce 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Ecommerce
    fields =['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ecommerce
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        ecommerce =self.get_object()
        if self.reuest.user == ecommerce.author:
            return True
        return False


class  PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Ecommerce
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
def about(request):
    return render(request, "app/about.html")
        

    



