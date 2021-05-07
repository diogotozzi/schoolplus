from django.http import JsonResponse
from django.views import View


class StudentView(View):

    def get(self, request, student_id=0):
        return JsonResponse({'student id': student_id})

    def post(self, request):
        pass

    def delete(self, request, student_id=0):
        pass


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