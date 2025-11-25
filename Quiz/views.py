from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializres import QuizSerializer

from .models import Quizes

# Create your views here.
@api_view(['GET'])
def quiz_list(request):
    quiz = Quizes.objects.all()
    serializer = QuizSerializer(quiz,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def add_quiz(request):
    is_many = isinstance(request.data, list)
    serializer = QuizSerializer(data =request.data, many = is_many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
