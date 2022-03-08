from django.contrib import admin
from django.urls import path
from englishman.views import EnglishView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EnglishView.as_view(), name='korean'),
]
