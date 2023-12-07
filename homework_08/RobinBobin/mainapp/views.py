from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Profile, Product
from .forms import ProfileCreateForm, ProductCreateForm

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="mainapp/index.html",
    )


class ProfilesList(ListView):
    model = Profile

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = "Profiles list"
        return context


class ProfilesDetail(DetailView):
    model = Profile

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context


class ProfilesCreate(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('profiles')


class ProductsList(ListView):
    model = Product

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products_list'] = "Products list"
        context['title'] = "Products list"
        return context


class ProductsDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context


class ProductsCreate(CreateView):
    model = Product
    form_class = ProductCreateForm
    success_url = reverse_lazy('products')