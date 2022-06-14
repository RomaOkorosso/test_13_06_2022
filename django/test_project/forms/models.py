from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=256)

    forms = models.ManyToManyField("Form", "UserForms", blank=True)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)


class Question(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)

    answers = models.ManyToManyField(Answer, related_name="answers")
    right_answers = models.ManyToManyField(Answer, related_name="right_answers")


class Form(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)

    questions = models.ManyToManyField(Question, blank=True)
    user = models.ManyToManyField(User, through="UserForms", blank=True)


class UserForms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
