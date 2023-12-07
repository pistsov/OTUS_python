from django.urls import path
from .views import (
    index,
    ProfilesList,
    ProfilesDetail,
    ProfilesCreate,
    ProductsList,
    ProductsDetail,
    ProductsCreate,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("profiles/", ProfilesList.as_view(), name="profiles"),
    path("profiles/add_profile/", ProfilesCreate.as_view(), name='add_profile'),
    path("profiles/<slug:pk>/", ProfilesDetail.as_view(), name="profile"),
    path("products/", ProductsList.as_view(), name="products"),
    path("products/add/", ProductsCreate.as_view(), name="add_product"),
    path("products/<slug:pk>/", ProductsDetail.as_view(), name="product"),
]