from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from api.v1.user.views import UserViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')


schema_view = get_schema_view(
    openapi.Info(title='Always data API', default_version='v1', description='Routes of Always data project'),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)


urlpatterns = [
    path('docs/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('', include((router.urls, 'api-root')), name='api-root'),
]
