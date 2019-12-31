from django.db import models

# Create your models here.


class Questions(models.Model):
    question_number = models.IntegerField()
    question_text = models.TextField()

    def __str__(self):
        return f'{self.question_number} {self.question_text}'


class Answers(models.Model):
    question_number = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()
    correct_answer = models.BooleanField()

