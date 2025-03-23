from calculator import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('admin/', admin.site.urls),
    path('omlet/', views.recipe_view, {'dish': 'omlet'}, name='omlet'),
    path('pasta/', views.recipe_view, {'dish': 'pasta'}, name='pasta'),
]
