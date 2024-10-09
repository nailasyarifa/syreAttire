from django import forms
from .models import ItemEntry
from django.utils.html import strip_tags

class ItemEntryForm(forms.ModelForm):
    class Meta:
        model = ItemEntry
        fields = ['name', 'category', 'size', 'color', 'price', ]

    def clean_item(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)