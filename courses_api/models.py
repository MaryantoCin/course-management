from django.db import models


class Course(models.Model):
    """Database model for course"""
    course_title = models.CharField(max_length=255)
    course_description = models.CharField(max_length=255)

    def __str__(self):
        return self.course_title

class Lesson(models.Model):
    """Database model for lesson"""
    lesson_title = models.CharField(max_length=255)

    def __str__(self):
        return self.lesson_title

class Material(models.Model):
    """Database model for material"""
    material_title = models.CharField(max_length=255)
    material_youtube_link = models.CharField(max_length=255)
