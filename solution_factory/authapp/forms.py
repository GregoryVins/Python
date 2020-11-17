from django.contrib.auth.forms import AuthenticationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):
    """Форма авторизации пользователя"""
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
