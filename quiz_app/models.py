from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question_num = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_char = models.CharField(max_length=20, default='A')

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choices = models.CharField(max_length=200, default='')


class Quiz(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
