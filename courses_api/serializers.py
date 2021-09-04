from rest_framework import serializers

from courses_api import models


class MaterialSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Material
    fields = ('id', 'lesson', 'material_title', 'material_description', 'material_youtube_link')
    extra_kwargs = {'lesson': {'required': False}}


class LessonSerializer(serializers.ModelSerializer):
  materials = MaterialSerializer(many=True)
  class Meta:
    model = models.Lesson
    fields = ('id', 'course', 'lesson_title', 'materials')
    extra_kwargs = {'course': {'required': False}}

class CourseSerializer(serializers.ModelSerializer):
  lessons = LessonSerializer(many=True)
  class Meta:
    model = models.Course
    fields = ('id', 'course_title', 'course_description', 'lessons')
    extra_kwargs = {'lessons': {'required': False}}

  def create(self, validated_data):
    lessons_data = validated_data.pop('lessons', None)
    newcourse = models.Course.objects.create(**validated_data)
    if lessons_data:
      for lesson_data in lessons_data:
        materials_data = lesson_data.pop('materials', None)
        newlesson = models.Lesson.objects.create(**lesson_data, course=newcourse)
        if materials_data:
          for material_data in materials_data:
            models.Material.objects.create(**material_data, lesson=newlesson)

    return newcourse

class LessonSerializer2(serializers.ModelSerializer):
  class Meta:
    model = models.Lesson
    fields = ('id', 'course', 'lesson_title')

class CourseSerializer2(serializers.ModelSerializer):
  class Meta:
    model = models.Course
    fields = ('id', 'course_title', 'course_description')


