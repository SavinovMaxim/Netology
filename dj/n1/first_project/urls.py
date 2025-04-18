from django.contrib import admin
from django.urls import path, include
from app.views import home_view, time_view, workdir_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('current_time/', time_view, name='current_time'),
    path('workdir/', workdir_view, name='workdir'),  
]
