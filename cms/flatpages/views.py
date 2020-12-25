from django.shortcuts import render
# Create your views here.

def first_page(request):
    return render(request, 'pages/first_page.html', {})