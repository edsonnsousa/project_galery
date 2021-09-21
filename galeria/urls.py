from django.contrib import admin
from django.template.backends import django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete/<int:list_id>/', views.delete, name='delete'),
    path('solicitacao/', views.solicitacao, name='solicitacao')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
