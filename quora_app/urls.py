from django.urls import path
from . import views

app_name = 'quora_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_question, name='create_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]
