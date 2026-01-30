from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page view - redirects logged-in users to dashboard"""
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:home')
        return super().get(request, *args, **kwargs)


class PricingView(TemplateView):
    """Pricing page view - redirects logged-in users to dashboard"""
    template_name = 'pricing.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:home')
        return super().get(request, *args, **kwargs)


class AboutView(TemplateView):
    """About Us page view"""
    template_name = 'about.html'
