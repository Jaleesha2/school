from django.urls import path
from . import views

urlpatterns = [
    path('home',views.teacher_home),
    path('signup',views.teacher_signup),
  

   
   
]
