from django.contrib import admin
from django.template.backends import django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    #path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete/<int:list_id>/', views.delete, name='delete'),
    path('solicitacao/', views.solicitacao, name='solicitacao'),
    path('aprovado/<int:list_id>', views.aprovado, name='aprovado'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name="cadastrar_usuario")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
