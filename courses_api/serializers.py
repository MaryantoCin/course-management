from rest_framework import serializers

from courses_api import models


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Course
    fields = ('id', 'course_title', 'course_description')
    

class LessonSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Lesson
    fields = ('id', 'course', 'lesson_title')
    

class MaterialSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Material
    fields = ('id', 'lesson', 'material_title', 'material_description', 'material_youtube_link')