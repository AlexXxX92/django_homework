from django.views.generic import ListView
from django.shortcuts import render

from .models import Student

# 4 запроса
# def students_list(request):
#     template = 'school/students_list.html'
#     object_list = Student.objects.all().order_by('group')
#     context = {'object_list': object_list}
#
#     return render(request, template, context)


# 2 запроса
def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.all().prefetch_related('teachers').order_by('group')
    context = {'object_list': object_list.all()}


    return render(request, template, context)
