from django.urls import path
from .views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),
    # Define other URLs as needed
]
