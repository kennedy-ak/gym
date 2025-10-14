from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user model with approval system"""
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_approved = models.BooleanField(default=False, help_text="Designates whether this user has been approved by admin.")
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-created_at']
