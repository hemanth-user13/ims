from django.db import models

# Create your models here.


class Student_data(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    department=models.CharField(max_length=100,default='CSE')
    class Meta:
        db_table = "Student_data"

    def __str__(self):
        return self.username


class Faculty_profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Faculty_Profile"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HOD_profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "HOD_Profile"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Files(models.Model):
    file_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Files"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class UploadedFiles(models.Model):
    file1 = models.FileField(upload_to='uploads/')
    file2 = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"UploadedFiles {self.id}"

class StudentFacultyMapping(models.Model):
    student_registration_number = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_branch = models.CharField(max_length=50)
    student_email = models.EmailField()
    faculty_name = models.CharField(max_length=100)
    faculty_email = models.EmailField()
    faculty_phone = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.student_name} - {self.faculty_name}"

from django.contrib.auth.models import User
class MyUploadedFiles(models.Model):
    weekly_report = models.FileField(upload_to='uploads/')
    certificate = models.FileField(upload_to='uploads/')
    ppt = models.FileField(upload_to='uploads/')
    final_project_report = models.FileField(upload_to='uploads/')
    student= models.ForeignKey(User, on_delete=models.CASCADE)

    # You can add fields to associate files with users or other data if needed

    def __str__(self):
        return f' {self.id} files'