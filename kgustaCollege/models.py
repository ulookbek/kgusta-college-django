from django.db import models
from django.utils import timezone

COURSE_OF_COLLEGE = (
    ('1', '1 курс'),
    ('2', '2 курс'),
    ('3', '3 курс'),
)


class Teachers(models.Model):
    full_name = models.CharField('ФИО', max_length=250, blank=False)
    position = models.CharField('Должность', max_length=250, blank=False)
    portrait = models.ImageField(upload_to='newsImg/', height_field=None,
                                 width_field=None, blank=False)
    description = models.TextField('Описание', blank=True)
    num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ['id']


class Events(models.Model):
    title = models.CharField('Заголовок события', max_length=250, blank=False)
    month = models.CharField('Месяц', max_length=250, blank=False)
    date_time = models.IntegerField()
    date_number = models.IntegerField()
    adress = models.CharField('Адрес', max_length=250, blank=False)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class Departments(models.Model):
    title = models.CharField('Название отделения', max_length=80, blank=False)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отделение"
        verbose_name_plural = "Отделения"


class AboutUs(models.Model):
    title = models.CharField('Заголовок галереи', max_length=250,
                             blank=True, null=True)
    file = models.FileField(upload_to='AboutUsPdfDocuments/', null=True,
                            blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class News(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField('Расписание', blank=False)
    images = models.ImageField(upload_to='galleryImg/', height_field=None,
                               width_field=None, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class OurGallery(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=True, null=True)
    description = models.TextField('Описание', blank=False)
    images = models.ImageField('Фотография', upload_to='galleryImg/', height_field=None,
                               width_field=None, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наша галерея"
        verbose_name_plural = "Наша галерея"

class ForEnrollee(models.Model):
    title = models.CharField('Название отделения', max_length=80, blank=False)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Абитуриентам"
        verbose_name_plural = "Абитуриентам"

class ForStudents(models.Model):
    title = models.CharField('Название отделения', max_length=80, blank=False)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Студентам"
        verbose_name_plural = "Студентам"
