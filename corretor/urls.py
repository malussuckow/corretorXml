from django.urls import path 
from corretor.views import corretor_View

urlpatterns = [
    path('', corretor_View, name='corretor')
]


