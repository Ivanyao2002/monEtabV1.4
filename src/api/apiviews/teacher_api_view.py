from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from teacher.models.teacher_model import TeacherModel
from ..serializers.teacher_serializer import TeacherSerializer


def teacher_list(request):
    pass

@csrf_exempt
def teacher_list(request):
    """
    Liste tous les professeurs, ou crée un nouveau professeur.
    """
    if request.method == 'GET':
        teachers = TeacherModel.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

