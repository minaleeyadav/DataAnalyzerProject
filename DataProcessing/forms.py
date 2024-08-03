from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a CSV file', help_text='max. 42 megabytes')
