from django.urls import path
from helloapp.views import *

urlpatterns = [
  path('', HelloWorldView.as_view(), name='hello_world'),
  path('<name>', HelloView.as_view(), name='hello_name'),
]