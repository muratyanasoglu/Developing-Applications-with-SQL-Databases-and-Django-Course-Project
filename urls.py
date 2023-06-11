from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [
    path('exam/<int:exam_id>/', views.exam_view, name='exam_view'),
    path('exam/<int:exam_id>/submit/', views.submit_exam, name='submit_exam'),
]
