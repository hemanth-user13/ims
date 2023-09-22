from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dashboard, name='main_dashboard'),
    path('student/login/', views.Student_Login, name='Student_Login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/register/', views.student_register, name='student_register'),
    path('faculty/login/', views.faculty_login, name='faculty_login'),
    path('hod/login/', views.hod_login, name='hod_login'),
    #path('upload/', views.upload_files, name='upload_files_page_url'),
    path('hod/dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('generate_mapping_excel/', views.generate_mapping_excel, name='generate_mapping_excel'),
    path('download_mapped_excel/', views.download_mapped_excel, name='download_mapped_excel'),
    path('mapping_list/', views.mapping_list, name='mapping_list'),
    path('student_files/', views.student_files, name='student_files'),
    path('faculty_dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
]
