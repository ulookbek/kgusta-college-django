from django.shortcuts import render

from kgustaCollege.models import Teachers, Events, Departments, News, AboutUs, \
    OurGallery, ForEnrollee, ForStudents


def main(request):
    all_events = Events.objects.all()[:4]
    all_news = News.objects.all()[:2]
    context = {
        "events": all_events,
        "news": all_news,
    }
    return render(request, 'home/home.html', context)


def about_us(request):
    return render(request, 'aboutUs/aboutUs.html')

def plans(request):
    return render(request, 'plans/plans.html')
    
def job_introduction(request):
    return render(request, 'job_introduction/job_introduction.html')

def directorate(request):
    return render(request, 'directorate/directorate.html')

def provisions(request):
    return render(request, 'provisions/provisions.html')

def for_enrolles(request):
    for_enrolles = ForEnrollee.objects.all()
    return render(request, 'for_enrolles/for_enrolles.html', {"for_enrolles": for_enrolles})

def for_students(request):
    for_students = ForStudents.objects.all()
    return render(request, 'for_students/for_students.html', {"for_students": for_students})

def students(request):
    students = ForStudents.objects.all()
    enrollees = ForEnrollee.objects.all()
    return render(request, 'students/students.html', {"students": students, "enrollees": enrollees})

def timetable(request):
    return render(request, 'timetable/timetable.html')


def contacts(request):
    return render(request, 'contacts/contacts.html')


def events(request):
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }

    return render(request, 'events/events.html', context)


def events_detail(request, id):
    event = Events.objects.get(id=id)
    context = {
        "event": event,
    }
    return render(request, 'events/event_detail.html', context)


def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {"news": news})


def departments(request):
    department = Departments.objects.all()
    return render(request, 'departments/departments.html',
                  {"departments": department})


def teacher_detail(request, id):
    curTeacher = Teachers.objects.get(id=id)
    return render(request, 'teachers/teacher_detail.html',
                  {"teacher": curTeacher})


def departments_detail(request, id):
    curDepartment = Departments.objects.get(id=id)
    return render(request, 'departments/departments_detail.html',
                  {"department": curDepartment})


def teachers(request):
    all_teachers = Teachers.objects.all().order_by('num')
    context = {
        "teachers": all_teachers,
    }
    return render(request, 'teachers/teachers.html', context)

