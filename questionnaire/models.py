from django.db import models

# Create your models here.


class Questionnaire(models.Model):
    name = models.CharField(max_length=20)

    SEX_CHOICES = (
        ('Boy', 'Boy'),
        ('Girl', 'Girl'),
        ('保密', '保密'),
    )
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='请选择')

    age = models.PositiveIntegerField(default=18)

    school = models.CharField(max_length=50)

    email = models.EmailField()

    def __str__(self):
        return self.name

