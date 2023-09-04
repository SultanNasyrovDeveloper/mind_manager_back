from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/node/', include('mind_palace.node.urls')),
    path('api/v1/palace/', include('mind_palace.palace.urls')),
    path('api/v1/learning/sessions/', include('mind_palace.learning_session.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)