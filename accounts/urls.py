from django.contrib import admin
from django.template.backends import django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
   #path('register/', views.SignUp.as_view(), name='register')
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
