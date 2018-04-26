from questionnaire.models import Questionnaire
from django import forms


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['name', 'sex', 'age', 'school', 'email']
