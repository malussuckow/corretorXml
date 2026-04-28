from django.urls import path
from home.views import home_View

urlpatterns = [
    path ('',home_View,name='home'), #home page
]