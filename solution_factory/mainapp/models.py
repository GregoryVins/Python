from django.db import models

from authapp.models import User


class Polling(models.Model):
    """
    Модель опроса. Стартовое время задаётся автоматически в момент создания опроса.
    """
    title = models.CharField(verbose_name='Тема опроса', max_length=64)
    description = models.CharField(verbose_name='описание', max_length=255, blank=True)
    start_time = models.DateTimeField(verbose_name='Дата и время начала', auto_now_add=True)
    end_time = models.DateTimeField(verbose_name='Дата и время окончания')

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    Модель вопросов, которые привязаны к опросу (один ко многим).
    Имеет три типа, которые передаются выбором.
    """
    SINGLE = 'S'
    MULTIPLE_CHOICES = 'M'
    TEXT_AREA = 'T'

    QUESTION_TYPE = (
        (SINGLE, 'Ответ с выбором одного варианта'),
        (MULTIPLE_CHOICES, 'Ответ с выбором нескольких вариантов'),
        (TEXT_AREA, 'Ответ вводом текста'),
    )

    polling = models.ForeignKey(Polling, verbose_name='Вопрос опроса', on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Текст вопроса', max_length=255)
    question_type = models.CharField(verbose_name='Тип вопроса', choices=QUESTION_TYPE, max_length=1, default=SINGLE)

    def __str__(self):
        return f'{self.text} ({self.polling.title})'


class Answer(models.Model):
    """
    Модель ответов на вопросы, имеет привязку к вопросу (один ко многим).
    """
    question = models.ForeignKey(Question, verbose_name='Ответ вопроса', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='Текст ответа', null=True)

    def __str__(self):
        return f'{self.text} ({self.question})'


class UserAnswer(models.Model):  # TODO: Доделать модель, подумать над более изящным решением
    """
    Модель пользовательского ответа на вопросы в опросах.
    В зависимости от типа вопроса предлагает ответ (текст или булево значение).
    Имеет связи (один ко многим) с опросом, вопросом и его ответами, а так же
    связь многие ко многим с пользователями.
    """
    answer_bool = models.BooleanField(default=False, blank=True)
    answer_text = models.TextField()
    answer = models.ForeignKey(Answer, verbose_name='ответ', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    poll = models.ForeignKey(Polling, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.answer_text
