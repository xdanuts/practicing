from django.urls import path
from dummyapp.views import index

app_name = 'dummyapp'

urlpatterns = [
   path('', view=index, name='index')
]
