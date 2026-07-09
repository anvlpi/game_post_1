from django.db import models


class TimeAndActive(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Game(TimeAndActive):
    global_name = models.CharField(max_length=128)
    active = models.BooleanField()


class GameTheme(TimeAndActive):
    game_id = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='games_themes'
    )
    theme_name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)


class QuestionTheme(TimeAndActive):
    game_theme_id = models.ForeignKey(
        GameTheme, on_delete=models.CASCADE, related_name='questions_theme'
    )
    theme = models.CharField(max_length=128)
    description = models.CharField(max_length=256)


class Question(TimeAndActive):
    question_theme_id = models.ForeignKey(
        QuestionTheme, on_delete=models.CASCADE, related_name='questions'
    )
    question = models.CharField(max_length=512)
    is_open = models.BooleanField(default=False)
    there_photo = models.BooleanField(default=False)
    there_music = models.BooleanField(default=False)
    photo_path = models.CharField(max_length=128)
    music_path = models.CharField(max_length=128)
