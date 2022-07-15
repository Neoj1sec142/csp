from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import MerchPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def merch(request):
    context = {
        'posts': MerchPost.objects.all()
    }
    return render(request, 'merch/home.html', context)

class MerchPostListView(ListView):
    model = MerchPost
    template_name = 'blog/home.html'
    context_object_name = "merchposts"
    ordering = ['-date_posted']
    paginate_by = 5


class MerchPostDetailView(DetailView):
    model = MerchPost

class MerchPostCreateView(LoginRequiredMixin, CreateView):
    model = MerchPost
    fields = ['title', 'description', 'price', 'catagory', 'img', ]
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class MerchPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MerchPost
    fields = ['title', 'description', 'price', 'catagory', 'img', ]
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class MerchPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MerchPost
    success_url = 'merch/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'merch/about.html', {'title': 'About'})
