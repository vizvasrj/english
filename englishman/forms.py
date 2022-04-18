from django import forms

class CommonWordsForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea()
    )
    num = forms.IntegerField()