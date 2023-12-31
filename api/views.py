from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def getAllStudent(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
