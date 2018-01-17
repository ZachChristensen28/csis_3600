from django.db import models
from django.utils import timezone
from django.urls import reverse


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    comments = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + ' - ' + '"' + self.comments + '"'

    def get_absolute_url(self):
        return reverse('contact:success')
