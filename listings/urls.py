from django.urls import path, include
from . import views

app_name = 'listings'  # Set the app name for reverse URL resolution

urlpatterns = [
    path('', views.home, name='home'),  # Homepage with random listings
    path('search/', views.search, name='search'),  # Search endpoint for listings
]
