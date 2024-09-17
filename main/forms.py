from django import forms
from .models import ItemEntry

class ItemEntryForm(forms.ModelForm):
    class Meta:
        model = ItemEntry
        fields = ['name', 'category', 'size', 'color', 'price', ]