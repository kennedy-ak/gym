from django.db import models
from django.conf import settings

# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('contacted', 'Contacted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    SERVICE_CHOICES = [
        ('gym_registration', 'Gym Registration - GHC 450'),
        ('full_body_massage', 'Full Body Massage - GHC 350 (In-House)'),
        ('neck_shoulder_pain', 'Neck & Shoulder Pain - GHC 250'),
        ('reflexo_therapy', 'Reflexo Therapy - GHC 250'),
        ('lower_back_shoulder', 'Lower Back & Shoulder - GHC 300'),
        ('deep_tissue_massage', 'Deep Tissue Massage - GHC 400 (In-House)'),
        ('home_full_body_massage', 'Full Body Massage - GHC 450 (Home Service)'),
        ('home_neck_shoulder', 'Neck & Shoulder Pain - GHC 350 (Home Service)'),
        ('home_reflexo', 'Reflexo Therapy - GHC 350 (Home Service)'),
        ('home_lower_back', 'Lower Back & Shoulder - GHC 400 (Home Service)'),
        ('home_deep_tissue', 'Deep Tissue Massage - GHC 500 (Home Service)'),
        ('driving_fatigue', 'Driving Fatigue - GHC 500 (Home Service)'),
    ]

    # User information
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    job_title = models.CharField(max_length=200, verbose_name="Job Title")
    location = models.CharField(max_length=200, verbose_name="Location/Area")
    address = models.TextField(verbose_name="Place Where You Stay", help_text="Your complete address")

    # Booking details
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, verbose_name="Service Requested")
    additional_notes = models.TextField(blank=True, verbose_name="Additional Notes (Optional)")

    # Status and metadata
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, help_text="Associated user account if logged in")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin_notes = models.TextField(blank=True, help_text="Internal notes for admin use")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"{self.full_name} - {self.get_service_display()} ({self.status})"

    def get_status_badge_class(self):
        """Return Bootstrap badge class based on status"""
        status_classes = {
            'pending': 'bg-warning',
            'contacted': 'bg-info',
            'completed': 'bg-success',
            'cancelled': 'bg-danger',
        }
        return status_classes.get(self.status, 'bg-secondary')
