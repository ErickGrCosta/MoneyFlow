from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('admin/', include('djoser.urls.authtoken')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('transactions.urls')),
]
