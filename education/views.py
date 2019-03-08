from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill, User, Question, Answer, Tag, Skill
from rest_framework.views import APIView
from .serializers import QuestionSerializer, AnswerSerializer, SkillSerializer, TagSerializer
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse("Hello World!")


class QuestionsAPI(APIView):
    def get(self, request, title, format=None):
        try:
            question = Question.objects.get(question_title=title)
            question_serializer = QuestionSerializer(question)
            question_data = question_serializer.data
            return Response(question_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No Question with the given title found.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, title, format=None):
        question_serializer = QuestionSerializer(data=request_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagsAPI(APIView):
    def get(self, request, question, format=None):
        try:
            tag = Tag.objects.filter(question=question)
            tag_serializer = TagSerializer(tag, many=True)
            tag_data = tag_serializer.data
            return Response(tag_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No tag found.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, title, format=None):
        tag_serializer = TagSerializer(data=request_data, many=True)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return Response(tag_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillAPI(APIView):
    def get(self, request, user, format=None):
        try:
            skill = Skill.objects.filter(user=user)
            skill_serializer = SkillSerializer(skill, many=True)
            skill_data = skill_serializer.data
            return Response(skill_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No such skill found.'}, status=status.HTTP_400_BAD_REQUEST)


class AnswerAPI(APIView):
    def get(self, request, question_id, format=None):
        try:
            answer = Answer.objects.filter(question=question_id)
            answer_serializer = AnswerSerializer(answer, many=True)
            answer_data = answer_serializer.data
            return Response(answer_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No Answer found.'}, status=status.HTTP_400_BAD_REQUEST)
