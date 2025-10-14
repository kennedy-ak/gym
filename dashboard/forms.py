from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for users to submit booking requests"""

    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number', 'job_title', 'location', 'address', 'service', 'additional_notes']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0244236973',
                'required': True
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Software Engineer, Teacher, etc.',
                'required': True
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Accra, Kumasi, etc.',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your complete address',
                'rows': 3,
                'required': True
            }),
            'service': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'additional_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any special requests or additional information (Optional)',
                'rows': 3
            }),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'job_title': 'Job Title',
            'location': 'Location/Area',
            'address': 'Complete Address (Where You Stay)',
            'service': 'Select Service',
            'additional_notes': 'Additional Notes (Optional)',
        }

    def __init__(self, *args, **kwargs):
        service = kwargs.pop('service', None)
        super().__init__(*args, **kwargs)

        # Pre-select service if provided via URL
        if service:
            self.fields['service'].initial = service
