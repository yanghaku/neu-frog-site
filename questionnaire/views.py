from django.shortcuts import render
from questionnaire.form import QuestionnaireForm
# Create your views here.


def question(request):
    if request.method == 'GET':
        form = QuestionnaireForm()
        return render(request, 'questionnaire/question.html', context={'form': form})
    else:
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'questionnaire/q_complete.html')
        else:
            return render(request, 'questionnaire/question.html', context={'form': form})
