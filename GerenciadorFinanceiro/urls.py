from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from polls.views import ContribuinteViewSet, UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Sua API",
        default_version='v1',
        description="Descrição da sua API",
    ),
    public=True,
)


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='Users')
router.register(r'contribuintes', ContribuinteViewSet, basename='Contribuintes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
