from django.urls import path
from .views import gallery, contact, index

urlpatterns = [
    path('',index, name='index'),
    path('gallery', gallery, name='gallery'),
    path('contact', contact, name='contact'),
]