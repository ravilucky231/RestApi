from .views import *
from django.urls import path

urlpatterns =[
    path('details/',details),
    path('create/',create),
    path('deleted/',deleted),
    path('update/',update),

]