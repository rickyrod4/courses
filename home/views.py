from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render (request, 'index.html', context)

def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    Course.objects.create(
        courseName = request.POST['courseName'],
        description = request.POST['description']
    )
    return redirect('/')

def remove(request, course_id):
    context = {
        'course' : Course.objects.get(id=course_id)
    }
    return render(request, 'remove.html',context)

def no(request):
    return redirect('/')

def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')