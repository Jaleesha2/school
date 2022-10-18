from django.shortcuts import render

# Create your views here.
def student_home(request):
    return render (request, 'students/home.html')

def student_signup(request):
    return render (request, 'students/signup.html')