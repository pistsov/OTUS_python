from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Profile, Product

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="mainapp/index.html",
    )


def profiles_list(request: HttpRequest) -> HttpResponse:
    profiles = (
        Profile
        .objects
        .order_by("pk")
        .all()
    )
    return render(
        request=request,
        template_name="profiles/profiles.html",
        context={"profiles": profiles},
    )


def get_profile_by_id(request: HttpRequest, profile_id: int) -> HttpResponse:
    profile = (
        Profile.objects.get(pk=profile_id)
    )

    return render(
        request=request,
        template_name="profiles/details.html",
        context={"profile": profile},
    )


def products_list(request: HttpRequest) -> HttpResponse:
    products = (
        Product
        .objects
        .order_by("pk")
    )
    return render(
        request=request,
        template_name="products/products.html",
        context={"products": products},
    )


def get_product_by_id(request: HttpRequest, product_id: int) -> HttpResponse:
    product = (
        Product.objects.get(pk=product_id)
    )
    return render(
        request=request,
        template_name="products/details.html",
        context={"product": product},
    )