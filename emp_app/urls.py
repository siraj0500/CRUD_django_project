from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empdb', views.empdb, name='empdb'),
    path('Delete/<int:id>/', views.empdelete, name='empdelete'),
    path('<int:id>/', views.empupdate, name='empupdate'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
