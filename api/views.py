from django.core.serializers import serialize
from django.http import JsonResponse
from django.views import View

from .models import Student

from datetime import datetime
import json


class StudentView(View):

    def get(self, request, student_id=None):
        if not student_id:
            students = Student.objects.filter(deleted=None).values()
            return JsonResponse({'result': list(students)}, status=200)

        student = Student.objects.filter(pk=student_id, deleted=None).values()

        if not student:
            return JsonResponse({'result': []}, status=404)

        return JsonResponse({'result': list(student)})

    def patch(self, request, student_id=None):
        if not student_id:
            return JsonResponse({'result': []}, status=400)

        student = Student.objects.filter(pk=student_id, deleted=None)

        if not student:
            return JsonResponse({'result': []}, status=404)

        # TODO: Use match statement in PEP 634 - https://www.python.org/dev/peps/pep-0634/
        changes = dict()
        for item in ['name', 'birthdate', 'rg', 'cpf']:
            if item == 'birthdate':
                changes[item] = datetime.strptime(request.PATCH['birthdate'], '%d/%m/%Y')
                continue
            changes[item] = request.PATCH[item] if item in request.PATCH else None

        student.update(**changes)

        return JsonResponse({'result': []}, status=200)

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
            return JsonResponse({'result': []}, status=400)

        student = Student.objects.get(pk=student_id, deleted=None)

        if not student:
            return JsonResponse({'result': []}, status=404)

        student.deleted = datetime.now()
        student.save()

        return JsonResponse({'result': []}, status=204)


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