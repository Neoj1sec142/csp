from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Merch
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def home(request):
    context = {
        'merchs': Merch.objects.all()
    }
    return render(request, 'merch-home', context)

class MerchListView(ListView):
    model = Merch
    template_name = 'merch-home'
    context_object_name = "merchs"
    ordering = ['-date_posted']
    paginate_by = 5


class MerchDetailView(DetailView):
    model = Merch

class MerchCreateView(LoginRequiredMixin, CreateView):
    model = Merch
    fields = ['title', 'description', 'price', 'catagory', 'img', ]
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class MerchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Merch
    fields = ['title', 'description', 'price', 'catagory', 'img', ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class MerchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Merch
    success_url = 'merch/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'merch/about.html', {'title': 'About'})