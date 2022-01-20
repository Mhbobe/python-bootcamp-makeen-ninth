from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(label='title',max_length=200)
    content = forms.CharField(label='add-up' , widget=forms.Textarea)