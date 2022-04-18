from django.urls import path 

from . import views

urlpatterns = [
    path('', views.common_words_view, name='common'),
    path('about-me/', views.about, name='about'),
    path('api-document/', views.api_doc, name='apidoc'),
]