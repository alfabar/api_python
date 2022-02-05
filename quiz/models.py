from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _

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

        title = models.CharField(max_length=255, default=_(
            "New Quiz"), verbose_name=("Quiz Title"))

    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):

    date_updated = models.DateField(
        verbose_name=_("Last Updated"), auto_now=True
    )
    class Meta:
        abstract = True


class Question(Updated):

    class Meta:
        verbose_name =_("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']


        SCALE =(
            (0, _('Fundamental')),
            (1, _('Beginner')),
            (2, _('Intermediario')),
            (3, _('Advanced')),
            (4, _('Expert')),

        )




    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    pass


class Answer(Updated):
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    pass
