from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render (request, 'index.html', context)