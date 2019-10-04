from django.urls import path,include
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',views.homePage,name='homepage'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
