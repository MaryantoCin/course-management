from rest_framework import serializers

from courses_api import models


class MaterialSerializer(serializers.ModelSerializer):
  """Serializes Material object"""
  class Meta:
    model = models.Material
    fields = ('id', 'lesson', 'material_title', 'material_description', 'material_youtube_link')
    extra_kwargs = {'lesson': {'required': False}}


class LessonSerializer(serializers.ModelSerializer):
  """Serializes Lesson Object"""
  class Meta:
    model = models.Lesson
    fields = ('id', 'course', 'lesson_title')

class CourseSerializer(serializers.ModelSerializer):
  """Serializes Nested Course object"""
  lessons = LessonSerializer(many=True)
  class Meta:
    model = models.Course
    fields = ('id', 'course_title', 'course_description', 'lessons')
    extra_kwargs = {'lessons': {'required': False}}

  def create(self, validated_data):
    """Handling inserting nested course"""
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

  def update(self, instance, validated_data):
    """Handling updating nested course"""
    instance.course_title = validated_data.get('course_title', instance.course_title)
    instance.course_description = validated_data.get('course_description', instance.course_description)
    instance.save()

    lessons_data = validated_data.pop('lessons', None)
    if lessons_data:
      for lesson_data in lessons_data:
        lesson = models.Lesson.objects.get(id=lesson_data.id)
        lesson.lesson_title = lesson_data.get('lesson_title', lesson.lesson_title)
        lesson.save()
        materials_data = lesson_data.pop('materials', None)
        if materials_data:
          for material_data in materials_data:
            material = models.Material.objects.filter(id=material_data.get('id'), lesson=lesson)
            material.material_title = material_data.get('material_title', material.material_title)
            material.material_description = material_data.get('material_description', material.material_description)
            material.material_youtube_link = material_data.get('material_youtube_link', material.material_youtube_link)
            material.save()
    
    return instance


class IndividualCourseSerializer(serializers.ModelSerializer):
  """Serializes Course Object"""
  class Meta:
    model = models.Course
    fields = ('id', 'course_title', 'course_description')


