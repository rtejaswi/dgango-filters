from django.db import models

# Create your models here.
class School(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length  = 30, unique = True)
    phno = models.CharField(max_length = 10, unique = True)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.first_name + self.last_name

class Student(models.Model):
    name = models.ForeignKey(School, on_delete = models.CASCADE)
    rollno = models.CharField(max_length = 15)
    def __str__(self):
        return str(self.rollno)
