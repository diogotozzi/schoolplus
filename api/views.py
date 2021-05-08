from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import Student

from datetime import datetime
import json


class StudentView(View):

    def get(self, request, student_id=None):
        if not student_id:
            return JsonResponse({}, status=400)

        student = get_object_or_404(Student, pk=student_id)
        # student = Student.objects.filter(pk=student_id, deleted=None)

        return JsonResponse(student, safe=False)

    def post(self, request):
        birthday = datetime.strptime(request.POST['birthdate'], '%d/%m/%Y')

        student = Student.objects.create(
            name = request.POST['name'],
            birthdate = birthday,
            rg = request.POST['rg'],
            cpf = request.POST['cpf'],
            created = datetime.now(),
        )

        return JsonResponse({'student_id': student.id}, status=201)

    def delete(self, request, student_id=None):
        if not student_id:
            return JsonResponse({}, status=400)

        student = get_object_or_404(Student, pk=student_id)
        student.deleted = datetime.now()
        student.save()

        return JsonResponse({}, status=204)


class TeacherView(View):

    def get(self, request, teacher_id):
        return JsonResponse({'teacher id': teacher_id})

    def post(self, request):
        pass

    def delete(self, request):
        pass


class ClassRoomView(View):

    def get(self, request, classroom_id):
        return JsonResponse({'classroom id': classroom_id})

    def post(self, request):
        pass

    def delete(self, request):
        pass


class GradeView(View):

    def get(self, request, grade_id):
        return JsonResponse({'grade id': grade_id})

    def post(self, request):
        pass

    def delete(self, request):
        pass