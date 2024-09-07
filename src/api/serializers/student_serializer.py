from student.models.student_model import StudentModel
from rest_framework.serializers import ModelSerializer


class StudentSerializer(ModelSerializer):

    class Meta:
        model = StudentModel
        fields = "__all__"