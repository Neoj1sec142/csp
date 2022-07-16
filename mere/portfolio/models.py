from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Portfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio-detail', kwargs={'pk': self.pk})

# class Picture(models.Model):
#     portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     img = models.ImageField(blank=True)
#     date_posted = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.title