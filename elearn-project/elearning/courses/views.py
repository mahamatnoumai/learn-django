from django.shortcuts import render
# Create your views here.

def my_first_view(request, who):
    return render(request, 'courses/hello.html')