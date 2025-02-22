from django.db import models

class Student(models.Model):
    student_nr = models.IntegerField()
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    mayor = models.CharField(max_length=80)
    role = models.CharField(max_length=20, blank=True, null=True)
    plant = models.IntegerField(blank=True, null=True)
    investigator = models.IntegerField(blank=True, null=True)
    coordinator = models.IntegerField(blank=True, null=True)
    shaper = models.IntegerField(blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    teamworker = models.IntegerField(blank=True, null=True)
    implementer = models.IntegerField(blank=True, null=True)
    finisher = models.IntegerField(blank=True, null=True)
    specialist = models.IntegerField(blank=True, null=True)


class Teacher(models.Model):
    teacher_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)


class Project(models.Model):
    project_nr = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, default="A fun interdisciplinary project!")
    teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)


class ProjectStudents(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_nr = models.IntegerField(blank=True, null=True)


class RoleTest(models.Model):
    role = models.CharField(max_length=20)
    question = models.TextField(max_length=300, default="Question")


class Role(models.Model):
    role = models.CharField(max_length=20)
    description = models.TextField(max_length=300, default="Description")