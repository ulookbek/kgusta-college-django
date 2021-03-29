from django.shortcuts import render

from kgustaCollege.models import Teachers, Events, Departments, News, AboutUs, \
    OurGallery, ForEnrollee, ForStudents


def main(request):
    all_events = Events.objects.all()[:4]
    context = {
        "events": all_events,
    }
    return render(request, 'home/home.html', context)


def about_us(request):
    about_us_info = AboutUs.objects.all()
    return render(request, 'aboutUs/aboutUs.html',
                  {"about_us_info": about_us_info})

# def abiturentos(request):
#     a = ForEnrollee.objects.all()
#     return render(request, 'enrollee/enrollee.html', {"enrollees": a})

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

