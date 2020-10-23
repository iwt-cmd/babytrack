from django import forms
from .models import BabyTrack, Baby

class DateInput(forms.DateInput):
    input_type = 'datetime-local'
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class EntryForm(forms.ModelForm):
    class Meta:
        model = BabyTrack
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

