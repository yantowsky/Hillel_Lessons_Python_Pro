from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('courses/', include('courses_app.urls')),
    path('members/', include('members_app.urls')),
    path('api/', include('courses_app.urls')),
    path('api/auth/', include('auth_app.urls')),

]
