from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.Cadastro_View, name='cadastro'),
    path('login/', views.Login_View, name='login'),
]