"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book library API",
        default_version='v1',
        description="Library demo project description",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="burgutlochin11@gmail.com"),
        license=openapi.License(name="Demo license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('book.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('api-auth/', include('rest_framework.urls')), # authenticate
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),  # authenticate
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('loaderio-d4d1e8bd6e1bd3cee210d30b68c7d72e/', )

]
