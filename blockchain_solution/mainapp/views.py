from django.shortcuts import render

from authapp.models import UserProfile
from mainapp.forms import UserSearchForm, MessagesForm
from mainapp.models import Message


def index(request):
    """
    Главная страница.
    Если пользователь авторизирован, в шаблоне рендерится меню поиска никнейма юзера.
    Если пользователь есть в БД, предоставляет ссылку на чат с пользователем,
    в противном случае отображает ошибку.
    """

    if request.method == 'POST':
        form = UserSearchForm(data=request.POST)
        if form.is_valid():
            nickname = request.POST['nickname']
            found_user = UserProfile.objects.filter(nickname=nickname).first()
            error = 'Пользователя с таким никнеймом не существует. ' \
                    'Проверьте правильность написания данного имени и регистра.'
            context = {
                'title': 'main page',
                'form': form,
                'found_user': found_user,
                'error': error,
            }
            return render(request, 'mainapp/index.html', context)
    else:
        form = UserSearchForm()

        context = {
            'title': 'main page',
            'form': form,
        }
        return render(request, 'mainapp/index.html', context)


def user_messages(request, pk):
    """
    Подгружает историю сообщений с пользователем.
    """
    recipient = UserProfile.objects.filter(pk=pk).first()
    recipient_messages = Message.objects.filter(sender=recipient, recipient=request.user).order_by('-created')
    sender_messages = Message.objects.filter(sender=request.user, recipient=recipient).order_by('-created')
    all_messages = recipient_messages | sender_messages

    if request.method == 'POST':
        form = MessagesForm(data=request.POST)
        if form.is_valid():
            sender = request.user
            message = request.POST['message']
            Message.objects.create(sender=sender, recipient=recipient, message=message)

            context = {
                'title': 'Messages',
                'recipient': recipient,
                'all_messages': all_messages,
                'form': form,
            }

            return render(request, 'mainapp/messages.html', context)

    else:
        form = MessagesForm()

        context = {
            'recipient': recipient,
            'all_messages': all_messages,
            'form': form,
        }

        return render(request, 'mainapp/messages.html', context)
