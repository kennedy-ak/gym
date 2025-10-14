from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import HealthTip, BlogPost
from .forms import BookingForm
from .models import Booking

@login_required
def dashboard_home(request):
    """Dashboard home view with health tips"""
    health_tips = HealthTip.objects.filter(is_active=True)[:5]
    recent_blogs = BlogPost.objects.filter(is_published=True).order_by('-published_at')[:3]

    context = {
        'health_tips': health_tips,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'dashboard/home.html', context)


def booking_form(request):
    """Handle booking form submission"""
    service = request.GET.get('service', '')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Associate with logged-in user if available
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()

            messages.success(
                request,
                'Your booking request has been submitted successfully! '
                'Our admin team will contact you soon.'
            )
            return redirect('dashboard:booking_success')
        else:
            messages.error(
                request,
                'There was an error with your submission. Please check the form and try again.'
            )
    else:
        form = BookingForm(service=service)

    context = {
        'form': form,
        'service': service,
    }
    return render(request, 'dashboard/booking_form.html', context)


def booking_success(request):
    """Booking success page"""
    return render(request, 'dashboard/booking_success.html')
