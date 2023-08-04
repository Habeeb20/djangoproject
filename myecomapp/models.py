from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Ecommerce(models.Model):
    name = models.CharField(max_length=60)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


