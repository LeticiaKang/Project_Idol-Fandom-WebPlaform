from django import forms
from .models import Image

class ImageUpload(forms.ModelForm):
    class Meta:
        model=Image
        fields=("image",)