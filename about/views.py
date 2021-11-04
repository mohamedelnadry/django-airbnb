from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import FAQ,About
# Create your views here.


class QustionDetail(ListView):
    model = FAQ

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last() 
        return context
    