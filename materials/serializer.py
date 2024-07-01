from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title', 'description',)


class CourseDetailSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_number_of_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons', 'number_of_lessons',)



