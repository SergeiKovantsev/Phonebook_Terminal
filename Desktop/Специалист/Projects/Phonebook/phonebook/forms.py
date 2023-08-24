from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['surname', 'name', 'patronymic', 'organization', 'work_phone', 'personal_phone']