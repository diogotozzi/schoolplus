from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('created')
    deleted = models.DateTimeField('deleted')


class Grade(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('created')
    deleted = models.DateTimeField('deleted')


class Student(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateTimeField('birthdate')
    rg = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(ClassRoom)
    created = models.DateTimeField('created')
    deleted = models.DateTimeField('deleted')


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    birthdate = models.DateTimeField('birthdate')
    rg = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    created = models.DateTimeField('created')
    deleted = models.DateTimeField('deleted')