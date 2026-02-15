from django.db import models


# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name}"
