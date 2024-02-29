from django.urls import path
from .views import index, shorten_url, redirect_to_original_url

urlpatterns = [
    path('', index, name='index'),
    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_code>/', redirect_to_original_url, name='redirect_to_original_url'),
]
