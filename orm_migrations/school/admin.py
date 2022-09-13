from django.contrib import admin

from .models import Student, Teacher


class MemberclassInline(admin.TabularInline):
    model = Student.teacher.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [MemberclassInline]
    include = ['student']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [MemberclassInline]

# Register your models here.
