from django import forms
from .models import Review

# Create a form without a model:
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label= "Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget = forms.Textarea, max_length=200)
#     raiting = forms.IntegerField(label = "Your Raiting", min_value = 1, max_value=5 )
  

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  
        fields = "__all__"
        labels = {
            "user_name": "your name",
            "review_text": "Your Feedback",
            "raiting": "Your Rating"
        }
        
        error_messages = {
            "required": "Your name must not be empty!",
            "max_length": "Please enter a shorter name!"
        }