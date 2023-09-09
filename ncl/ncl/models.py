from django.db import models

class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class StudentXCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course.name}"
  
class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ProfessorXCourse(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.professor.first_name} {self.professor.last_name} - {self.course.name}"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_date = models.DateField()
    reference_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.amount}"

class Inscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, unique=True)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)