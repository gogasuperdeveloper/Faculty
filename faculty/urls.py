from django.urls import path
from . import views

app_name = "faculty"

urlpatterns = [
    path("", views.home, name="home"),
    path("programs/", views.programs, name="programs"),
    path("programs/<int:id>/", views.program_detail, name="program_detail"),
    path("departments/", views.departments, name="departments"),
    path("departments/<int:id>/", views.department_detail, name="department_detail"),
]