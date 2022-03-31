from django.urls import path
from . import views

urlpatterns = [
    # path("category/", views.categories),
    # path('cat_det/', views.select_category),
    # path('products/', views.products),
    path('products/', views.product_union_with_category),
    path('products_not/', views.not_product),
]