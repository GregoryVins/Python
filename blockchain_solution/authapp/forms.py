import django.forms as forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import UserProfile


class UserLoginForm(AuthenticationForm):
    """Форма авторизации пользователя"""
    class Meta:
        model = UserProfile
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class UserRegisterForm(UserCreationForm):
    """Форма регистриции нового пользователя"""
    class Meta:
        model = UserProfile
        fields = (
            'username', 'password1', 'password2', 'email', 'nickname',
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''


class UserUpdateForm(UserChangeForm):
    """Форма обновления информации пользователя"""
    class Meta:
        model = UserProfile
        fields = (
            'username', 'password', 'nickname', 'email', 'first_name', 'last_name',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = forms.HiddenInput()
            else:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
