from django.urls import path
from api.views import StudentView, TeacherView, ClassRoomView, GradeView

from . import views

urlpatterns = [
    path('student', StudentView.as_view()),
    path('student/<int:student_id>', StudentView.as_view()),
    path('teacher', TeacherView.as_view()),
    path('teacher/<int:teacher_id>', TeacherView.as_view()),
    path('classroom', ClassRoomView.as_view()),
    path('classroom/<int:classroom_id>', ClassRoomView.as_view()),
    path('grade', GradeView.as_view()),
    path('grade/<int:grade_id>', GradeView.as_view()),
]