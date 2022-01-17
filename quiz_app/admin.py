from django.contrib import admin

from .models import Quiz, Question, Choice, Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'choices')


class QuizAdmin(admin.ModelAdmin):
    list_display = ('text',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'id')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_correct', 'question', 'choice_char')


admin.site.register(Answer, AnswerAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
