from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class MerchPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)
    img = models.ImageField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('merch-detail', kwargs={'pk': self.pk})