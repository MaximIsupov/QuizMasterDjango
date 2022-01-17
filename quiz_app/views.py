from django.shortcuts import render
from .models import Question, Choice, Answer, Quiz
from .consts import NUMBER_OF_QUESTIONS
from quiz import services, dto


def main_page(request):
    first_question = Question.objects.first()
    quiz = Quiz.objects.first()
    context = {'question': first_question,
               'quiz': quiz}
    return render(request, 'quiz_app/main.html', context)


def load_question(request, question_id):
    question = Question.objects.get(id=question_id)
    prev_question_id = question_id - 1
    choices = Choice.objects.filter(question=question_id)
    create_or_upload_answer(request, prev_question_id)
    if question_id != NUMBER_OF_QUESTIONS:
        next_question_id = question_id + 1
    else:
        next_question_id = 0
    context = {'question': question,
               'choices': choices,
               'next_question_id': next_question_id,
               'prev_question_id': prev_question_id}
    return render(request, 'quiz_app/question_page.html', context)


def finish_page(request):
    first_question = Question.objects.first()
    create_or_upload_answer(request, NUMBER_OF_QUESTIONS)
    context = {'question': first_question}
    return render(request, 'quiz_app/finish_page.html', context)


def create_or_upload_answer(request, question_id):
    if request.GET:
        prev_values = request.GET
        if not Answer.objects.filter(question=question_id).exists():
            question = Question.objects.get(id=question_id)
            answer = Answer()
            answer.question = question
            answer.choices = ','.join(prev_values.getlist('answer'))
            answer.save()
        else:
            answer = Answer.objects.get(question=question_id)
            answer.choices = ','.join(prev_values.getlist('answer'))
            answer.save(update_fields=['choices'])


def result_page(request):
    questions = Question.objects.all()
    quiz = Quiz.objects.first()
    answers = Answer.objects.all()
    questions_list = []
    answers_list = []
    for question in questions:
        question_uuid = question.id
        question_text = question.text
        choices_list = []
        for choice in Choice.objects.filter(question=question.id):
            choice_dto = services.ChoiceDTO(uuid=choice.id,
                                            text=choice.text,
                                            is_correct=choice.is_correct)
            choices_list.append(choice_dto)
        question_dto = dto.QuestionDTO(uuid=question_uuid,
                                       text=question_text,
                                       choices=choices_list)
        questions_list.append(question_dto)
    quiz_dto = dto.QuizDTO(uuid=quiz.id,
                           title=quiz.text,
                           questions=questions_list)
    for answer in answers:
        answer_dto = dto.AnswerDTO(question_uuid=answer.question.id,
                                   choices=answer.choices.split(','))
        answers_list.append(answer_dto)
    answers_dto = dto.AnswersDTO(quiz_uuid=quiz.id,
                                 answers=sorted(answers_list, key=lambda x: x[0]))
    quiz_result_service = services.QuizResultService(quiz_dto=quiz_dto,
                                                     answers_dto=answers_dto)
    result = quiz_result_service.get_result()
    context = {'result': result}
    return render(request, 'quiz_app/result_page.html', context)
