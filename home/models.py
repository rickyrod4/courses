from django.db import models

class CourseManager(models.Manager):
    def validate(request, form_data):
        errors = {}
        if len(form_data['courseName']) < 5:
            errors['courseName'] = 'Course Name must be at lease 5 characters'
        if len(form_data['description']) < 10:
            errors['description'] = 'Description must contain at least 10 characters'

        return errors
            


# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()