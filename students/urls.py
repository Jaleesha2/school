from django.urls import path
from . import views

urlpatterns = [
    path('home',views.student_home),
    path('signup',views.student_signup),
  

   
   
]