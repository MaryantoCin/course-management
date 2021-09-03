from django.db import models


class Course(models.Model):
    """Database model for course"""
    course_title = models.CharField(max_length=255)
    course_description = models.TextField()

    def __str__(self):
        return self.course_title

class Lesson(models.Model):
    """Database model for lesson"""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    lesson_title = models.CharField(max_length=255)

    def __str__(self):
        return self.lesson_title

class Material(models.Model):
    """Database model for material"""
    lesson = models.ForeignKey(
        Lesson, 
        on_delete=models.CASCADE,
        related_name='materials'
    )
    material_title = models.CharField(max_length=255)
    material_description = models.TextField()
    material_youtube_link = models.URLField(max_length=255)

    def __str__(self):
        return self.material_title
