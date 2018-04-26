from django.contrib import admin
from questionnaire.models import Questionnaire
# Register your models here.


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'school', 'age', 'email']
    list_filter = ['sex', 'school', 'age']


admin.site.register(Questionnaire, QuestionnaireAdmin)
