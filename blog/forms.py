from django import forms 

from .models import Comment

class CommentForm(forms.ModelsForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']