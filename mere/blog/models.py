
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    catagory = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
