from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    preview = models.ImageField(upload_to="media/course", verbose_name="Изображение", **NULLABLE)
    description = models.TextField(verbose_name="Описание курса", **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название урока")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    preview = models.ImageField(upload_to="media/lesson", verbose_name="Изображение", **NULLABLE)
    video_url = models.URLField(verbose_name="Ссылка на видео", **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"



