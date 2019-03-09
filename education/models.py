from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_moderator = models.BooleanField(default=True)
    available_mentor = models.BooleanField(default=True)
    available_mentee = models.BooleanField(default=True)
    assigned_mentor = models.ForeignKey("User",on_delete=models.CASCADE,blank=True, null=True)
    reputation = models.IntegerField(default=0)
    bio = models.CharField(max_length=200,default="Tell about yourself")

    def __str__(self):
        return str(self.username)

    def __unicode__(self):
        return str(self.username)

class Skill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=1200, blank=False, null=False)

    def __str__(self):
        return str(self.user.username) + " - " + str(self.name)

    def __unicode__(self):
        return str(self.user.username) + " - " + str(self.name)

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    question_title = models.CharField(max_length=200, blank=True, null=True)
    question_description = models.CharField(max_length=2000, blank=True, null=True)
    question_upvotes = models.IntegerField(default=0)
    question_downvotes = models.IntegerField(default=0)
    bider = models.ForeignKey(User, related_name='bider_for_a_question', blank=True, null=True)

    def __str__(self):
        return str(self.question_title)

    def __unicode__(self):
        return str(self.question_title)

class Tag(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,blank=True,null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.tag)

    def __unicode__(self):
        return str(self.tag)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    answer_text = models.CharField(max_length=5000, blank=True, null=True)
    answer_upvotes = models.IntegerField(default=0)
    answer_downvotes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.question.question_title)

    def __unicode__(self):
        return str(self.question.question_title)