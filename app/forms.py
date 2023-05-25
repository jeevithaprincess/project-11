from app.models import *
from django import forms
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['tname']
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url','email']
class AccessRecordsForm(forms.ModelForm):
     class Meta:
        model=AccessRecords
        fields=['author','date']
