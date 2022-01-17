from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('finish/', views.finish_page, name='finish_page'),
    path('result/', views.result_page, name='result_page'),
    path('question/<int:question_id>', views.load_question, name='question_page'),
]