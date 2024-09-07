from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from student.models.student_model import StudentModel
from ..serializers.student_serializer import StudentSerializer


def student_list(request):
    pass

@csrf_exempt
def student_list(request):
    """
    Liste tous les élèves, ou crée un nouveau élève.
    """
    if request.method == 'GET':
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

