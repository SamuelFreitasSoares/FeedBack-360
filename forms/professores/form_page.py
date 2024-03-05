from django import forms
from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['text', 'option1', 'option2', 'option3', 'option4', 'option5']
    
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['option1'].widget.attrs.update({'class': 'form-control'})
        self.fields['option2'].widget.attrs.update({'class': 'form-control'})
        self.fields['option3'].widget.attrs.update({'class': 'form-control'})
        self.fields['option4'].widget.attrs.update({'class': 'form-control'})
        self.fields['option5'].widget.attrs.update({'class': 'form-control'})


class UploadFileForm(forms.Form):
    file = forms.FileField()
    
    