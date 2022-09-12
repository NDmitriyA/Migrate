
from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'students_list.html'
    ordering = 'group'
    students = Student.objects.order_by(ordering)
    context = {
        'students': students
    }

    return render(request, template, context)