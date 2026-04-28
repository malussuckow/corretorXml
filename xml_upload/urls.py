from django.urls import path
from xml_upload import views

urlpatterns = [
    path('', views.upload_xml, name='upload'),
]