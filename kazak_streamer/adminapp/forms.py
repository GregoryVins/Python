from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from authapp.forms import forms
from mainapp.models import Category, Product


class AdminUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'password1', 'password2', 'email'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class AdminUserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'is_superuser',
            'password', 'email', 'is_active', 'is_staff'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class AdminCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AdminProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
