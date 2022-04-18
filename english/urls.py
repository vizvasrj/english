from django.contrib import admin
from django.urls import path, include
from englishman.views import EnglishView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', EnglishView.as_view(), name='api'),
    path('', include('englishman.urls')),
]
