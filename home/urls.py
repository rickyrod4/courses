from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('remove/<int:course_id>', views.remove),
    path('no', views.no),
    path('delete/<int:course_id>', views.delete)
]