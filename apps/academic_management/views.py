from django.shortcuts import redirect, render
from .models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, "course_management.html", {"courses": courses})


def registerCourse(request):
    code = request.POST["txtCode"]
    name = request.POST["txtName"]
    credits = request.POST["numCredits"]
    course = Course.objects.create(code=code, name=name, credits=credits)
    return redirect("/")


def editCourse(request, code):
    course = Course.objects.get(code=code)
    return render(request, "courseEdition.html", {"course": course})


def deleteCourse(request, code):
    course = Course.objects.get(code=code)
    course.delete()

    return redirect("/")


def courseEdition(request):
    code = request.POST["txtCode"]
    name = request.POST["txtName"]
    credits = request.POST["numCredits"]

    course = Course.objects.get(code=code)
    course.name = name
    course.credits = credits
    course.save()

    return redirect("/")
