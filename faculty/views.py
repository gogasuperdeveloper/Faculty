from django.shortcuts import render, get_object_or_404
from .models import Department, Program, HomePage, ExchangeProgram


def home(request):
    page = HomePage.objects.first()
    return render(request, "faculty/home.html", {"page": page})


def programs(request):
    programs = Program.objects.all()
    return render(request, "faculty/programs.html", {"programs": programs})


def program_detail(request, id):
    program = get_object_or_404(Program, id=id)
    return render(request, "faculty/program_detail.html", {"program": program})


def departments(request):
    departments = Department.objects.all()
    return render(request, "faculty/departments.html", {"departments": departments})


def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(request, "faculty/department_detail.html", {"department": department})


def exchange(request):
    programs = ExchangeProgram.objects.all()
    return render(request, "faculty/exchange.html", {"programs": programs})