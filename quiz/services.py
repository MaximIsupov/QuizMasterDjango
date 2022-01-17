from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


def get_correct_choices(choices):
    correct_choices = []
    for choice in choices:
        if choice.is_correct:
            correct_choices.append(str(choice.uuid))
    return correct_choices


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        result = 0
        price_for_the_choice = self.get_price_for_the_choice()
        for answer in self.answers_dto.answers:
            for question in self.quiz_dto.questions:
                if answer.question_uuid == question.uuid:
                    correct_choices = get_correct_choices(question.choices)
                    if len(set(correct_choices) & set(answer.choices)) == len(correct_choices):
                        result += price_for_the_choice
        return round(result, 2)

    def get_price_for_the_choice(self):
        return 1 / len(self.answers_dto.answers)
