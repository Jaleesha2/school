from django.shortcuts import render

# Create your views here.
def teacher_home(request):
    return render (request, 'teacher/home.html')

def teacher_signup(request):
    return render (request, 'teacher/teacher_signup.html')