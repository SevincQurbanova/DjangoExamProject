from django.urls import path, include
from django.contrib import admin
from app.views import RegisterView, LoginView, home, DepartmentViewSet, PositionViewSet, EmployeeViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.i18n import i18n_patterns

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# i18n_patterns for language-aware URLs
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', home, name='home'),
    path('', include(router.urls)),
)

# Add the following for language switching support
