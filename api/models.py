from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateField('created', null=True)
    deleted = models.DateField('deleted', null=True, db_index=True)


class Grade(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateField('created', null=True)
    deleted = models.DateField('deleted', null=True, db_index=True)


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    birthdate = models.DateField('birthdate', null=True)
    rg = models.CharField(max_length=14, null=True)
    cpf = models.CharField(max_length=14, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    classrooms = models.ManyToManyField(ClassRoom, null=True)
    created = models.DateField('created', null=True)
    deleted = models.DateField('deleted', null=True, db_index=True)


class Teacher(models.Model):
    name = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, null=True)
    birthdate = models.DateField('birthdate', null=True)
    rg = models.CharField(max_length=14, null=True)
    cpf = models.CharField(max_length=14, null=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, null=True)
    created = models.DateField('created', null=True)
    deleted = models.DateField('deleted', null=True, db_index=True)