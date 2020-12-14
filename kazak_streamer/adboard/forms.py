import django.forms as forms

from adboard.models import Ad


class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
