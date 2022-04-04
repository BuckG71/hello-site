from django.urls import path
from goodbyeapp.views import *

urlpatterns = [
  path('', GoodbyeWorldView.as_view(), name='goodbye_world'),
  path('<name>', GoodbyeView.as_view(), name='goodbye_name'),
]


 