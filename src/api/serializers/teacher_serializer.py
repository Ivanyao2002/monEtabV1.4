from teacher.models.teacher_model import TeacherModel
from rest_framework.serializers import ModelSerializer


class TeacherSerializer(ModelSerializer):

    class Meta:
        model = TeacherModel
        fields = "__all__"