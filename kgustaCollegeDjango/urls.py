from django.contrib import admin
from django.urls import path, include
from kgustaCollege import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.main, name='mainPages'),
                  path('about-us/', views.about_us, name='about-us'),
                  path('plans/', views.plans, name='plans'),
                  path('directorate/', views.directorate, name='directorate'),
                  path('job_introduction/', views.job_introduction, name='job_introduction'),
                  path('provisions/', views.provisions, name='provisions'),
                  path('timetable/', views.timetable, name='timetable'),
                  path('contacts/', views.contacts, name='contacts'),
                  path('events/', views.events, name='events'),
                  path('events_detail/<int:id>/', views.events_detail,
                       name='events_detail'),
                  path('news/', views.news, name='news'),
                  path('departments/', views.departments, name='departments'),
                  path('departments_detail/<int:id>/', views.departments_detail,
                       name='department_detail'),
                  path('teachers/', views.teachers, name='teachers'),
                  path('students/', views.students, name='students'),
                  path('for_enrolles/', views.for_enrolles, name='for_enrolles'),
                  path('for_students/', views.for_students, name='for_students'),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('teacher_detail/<int:id>/', views.teacher_detail,
                       name='teacher_detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
