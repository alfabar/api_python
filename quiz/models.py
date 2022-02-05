from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    pass

class Question(UpdatedQuestio):
    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    pass

class Answer(UpdatedQuestion):
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    pass