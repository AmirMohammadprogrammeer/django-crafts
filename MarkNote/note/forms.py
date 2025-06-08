from django import forms
from .models import Comment,Note

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["slug","title","body","status"]