from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    news = models.CharField(max_length=280)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.news
    
    class Meta:
        ordering = ['-date']


class Learn(models.Model):
    title = models.CharField(max_length=280)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('learn_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
