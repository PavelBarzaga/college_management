from django.shortcuts import render
from .models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, "course_management.html", {"courses": courses})
