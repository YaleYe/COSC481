from django.urls import path
from . import  views


#import views into URL
urlpatterns = [
    path("",views.signin),
]
