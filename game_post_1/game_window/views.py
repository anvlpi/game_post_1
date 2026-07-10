from django.shortcuts import render
from .models import QuestionTheme


def get_game_window(request, id=None):
    context = dict()
    # Получить темы вопросов из выбранной темы игры
    themes = QuestionTheme.objects.all().filter(active=True, game_theme_id=id)
    # Словарное включение для каждой темы
    context['themes'] = {theme: None for theme in themes}

    # Переберем каждую тему и закинем по ключу темы вопросы
    for theme in context['themes']:
        # Через обратную ссылку (см. в модели), получим все вопросы данной темы
        questions = theme.questions.filter(active=True)
        context['themes'][theme] = questions

    # Что бы не потерять вложенность, пока не перенес в шаблон
    # for theme in context['themes']:
    #     for question in context['themes'][theme]:
    #         print(question.question)

    return render(request, 'game_window/game.html', context)
