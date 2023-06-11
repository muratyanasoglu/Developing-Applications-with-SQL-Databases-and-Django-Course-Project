from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Exam, Question, Choice

def exam_view(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exams/exam_view.html', {'exam': exam})

def submit_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    try:
        selected_choices = {k: request.POST[k] for k in request.POST if k.startswith('choice')}
    except KeyError:
        return render(request, 'exams/exam_view.html', {
            'exam': exam,
            'error_message': "You didn't complete the exam.",
        })
    else:
        correct_answers = 0
        total_questions = exam.question_set.count()
        for question_id, choice_id in selected_choices.items():
            question = Question.objects.get(id=question_id)
            choice = Choice.objects.get(id=choice_id)
            if choice.is_correct:
                correct_answers += 1
        result = correct_answers / total_questions * 100
        return render(request, 'exams/result.html', {'result': result, 'exam': exam})
