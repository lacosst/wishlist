from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('wisher/<int:pk>/', list_page, name='wish_list_page')
]
