from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def home(request):
    context = {
        'portfolios': Portfolio.objects.all()
    }
    return render(request, 'portfolio-home', context)

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio-home'
    context_object_name = "portfolios"
    ordering = ['-date_posted']
    paginate_by = 5


class PortfolioDetailView(DetailView):
    model = Portfolio

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ['title', 'description', 'img', ]
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Portfolio
    fields = ['title', 'description', 'img', ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PortfolioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Portfolio
    success_url = 'portfolio/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About'})