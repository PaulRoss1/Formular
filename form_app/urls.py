from django.urls import path
from . import views

app_name = 'form_app'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
]
