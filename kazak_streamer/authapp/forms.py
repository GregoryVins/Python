import django.forms as forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SchoolUserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class SchoolUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''


class SchoolUserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 'password', 'email', 'first_name', 'last_name'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = forms.HiddenInput()
            else:
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''
