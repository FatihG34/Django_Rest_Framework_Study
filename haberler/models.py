from django.db import models

# Create your models here.


class Makele(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    content = models.TextField()
    country = models.CharField(max_length=120)
    published_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title