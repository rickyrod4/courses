from django.db import models

# Create your models here.
class Course(models.Model):
    courseName = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)