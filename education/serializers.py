from rest_framework import serializers
from .models import User, Question, Skill, Tag, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('user', 'question_title', 'question_description', 'question_upvotes', 'question_downvotes')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('user','question', 'answer_text', 'answer_upvotes', 'answer_downvotes')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag', 'question')

class SkilllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('user', 'name')


