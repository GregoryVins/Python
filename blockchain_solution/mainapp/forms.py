import django.forms as forms


class UserSearchForm(forms.Form):
    """Форма поиска пользователя."""
    nickname = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nickname'].widget.attrs.update({'class': 'form-control'})


class MessagesForm(forms.Form):
    """Форма отправки сообения."""
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
