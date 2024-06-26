from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Sum
User = get_user_model()



class Recipe(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True , blank= True)
  recipe_name = models.CharField(max_length=200)
  recipe_description = models.TextField()
  recipe_image = models.ImageField(upload_to="recipe")

class Department(models.Model):
  department = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.department
  class Meta:
    ordering = ['department']
class Subject(models.Model):
  subject_name = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.subject_name

class StudentID(models.Model):
  student_id = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.student_id

class Student(models.Model):
  department = models.ForeignKey(Department , related_name="depart", on_delete=models.CASCADE)
  student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
  student_name = models.CharField(max_length=100)
  student_age = models.IntegerField(default=18)
  student_email = models.EmailField(unique=True)
  student_address = models.TextField()

  def __str__(self) -> str:
    return self.student_name
  
  class Meta:
    ordering = ['student_name']
    verbose_name = 'student'

class SubjectMarks(models.Model):
  student = models.ForeignKey(Student , related_name="studentmarks", on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  marks = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.student.student_name} {self.subject.subject_name}'
  class Meta:
    unique_together = ['student', 'subject']

class ReportCard(models.Model):
  student = models.ForeignKey(Student , related_name="studentreportcard", on_delete=models.CASCADE)
  student_rank = models.IntegerField()
  date_of_reportCard_generation = models.DateField(auto_now_add=True)

  class Meta:
    unique_together = ['student_rank', 'date_of_reportCard_generation']


