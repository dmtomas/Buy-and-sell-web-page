from django.urls import path
from . import views
from .views import process_order
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('process_order/', process_order, name='process_order'),
]