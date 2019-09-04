from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='Enter your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Name'
            }
        )
    )
    rating=forms.IntegerField(
        label='Enter your Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter rating'
            }
        )
    )
    feedback=forms.CharField(
        label='Enter your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Feedback'
            }
        )
    )