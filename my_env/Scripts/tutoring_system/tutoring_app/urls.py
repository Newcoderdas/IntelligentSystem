from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tutoring_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.exercise_view, name='exercise')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
