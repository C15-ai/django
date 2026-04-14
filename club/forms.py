from django import forms
class ClubForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    founded_year = forms.IntegerField()

