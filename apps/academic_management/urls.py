from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("registerCourse/", views.registerCourse),
    path("deleteCourse/<code>", views.deleteCourse),
    path("editCourse/<code>", views.editCourse),
    path("courseEdition/", views.courseEdition),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
