from django.contrib import admin

# Register your models here.
from .models import Student_data
admin.site.register(Student_data)
from .models import Faculty_profile
admin.site.register(Faculty_profile)
from .models import HOD_profile
admin.site.register(HOD_profile)


from .models import UploadedFiles
admin.site.register(UploadedFiles)

from.models import  StudentFacultyMapping
admin.site.register(StudentFacultyMapping)

from.models import MyUploadedFiles
admin.site.register(MyUploadedFiles)