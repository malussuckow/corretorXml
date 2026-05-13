from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
]