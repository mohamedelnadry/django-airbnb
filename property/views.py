from django.db import models
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import ListView, DetailView,CreateView
from .models import Property,Category,PropertyImages,PropertyReview
from .forms import property_form
from django.views.generic.edit import FormMixin
from django.contrib import messages
from .filters import PropertyFilter
# Create your views here.

class PropertyList(ListView):
    model = Property
    template_name = 'property_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = PropertyFilter(self.request.GET,queryset=self.get_queryset())
        return context
    
    def get_queryset(self):
        peropert_list = super().get_queryset()
        
        return PropertyFilter(self.request.GET,queryset=peropert_list).qs
    
    

class PropertyDetails(FormMixin, DetailView):
    model = Property
    form_class = property_form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["property_img"] = PropertyImages.objects.filter(property=self.get_object().id)
        context["get_reltated"] = Property.objects.filter(category=self.get_object().category)[:3]
        context['review_count'] = PropertyReview.objects.filter(property=self.get_object()).count()
        return context
    
    def post(self,request,*args, **kwargs):
        slug = self.get_object().slug
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.save()
            messages.success(request, 'resestraion successfully')
            return redirect(reverse("property:propertyDetail", kwargs={'slug': slug}))


class property_new(CreateView):
    model = Property
    fields = ['title','description','price','place','image','category']
    
    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'property added successfully')
            return redirect(reverse("property:propertyList"))
