from .import views
from django.urls import path

app_name = 'store'

urlpatterns = [
    path('', views.products_all, name='all_products'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]