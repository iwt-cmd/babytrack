from django import forms
from .models import BabyTrack

class PostForm(forms.ModelForm):
    class Meta:
        model = BabyTrack
        fields = ['name', 'date', 'wet', 'dirty', 'leftside', 'rightside', 'sup_amount', 'sup_f', 'sup_b']