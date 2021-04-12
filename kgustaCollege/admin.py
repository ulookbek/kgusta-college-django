from django.contrib import admin
from django.contrib.gis import forms

from .models import Teachers, Events, Departments, News, AboutUs, OurGallery, ForEnrollee, ForStudents

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DepartmentsAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание",
                                  widget=CKEditorUploadingWidget())

    class Meta:
        model = Departments
        fields = '__all__'

class EnrolleesAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание",
                                  widget=CKEditorUploadingWidget())

    class Meta:
        model = ForEnrollee
        fields = '__all__'

class StudentsAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание",
                                  widget=CKEditorUploadingWidget())

    class Meta:
        model = ForStudents
        fields = '__all__'


# @admin.register(Teachers)
# class CollegeAdmin(admin.ModelAdmin):
#     pass


@admin.register(News)
class CollegeAdmin(admin.ModelAdmin):
    pass

@admin.register(Departments)
class CollegeAdmin(admin.ModelAdmin):
    form = DepartmentsAdminForm

@admin.register(ForEnrollee)
class CollegeAdmin(admin.ModelAdmin):
    form = EnrolleesAdminForm

@admin.register(ForStudents)
class CollegeAdmin(admin.ModelAdmin):
    form = StudentsAdminForm

@admin.register(Events)
class CollegeAdmin(admin.ModelAdmin):
    pass