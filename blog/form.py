from django import forms
from .models import Post

class PostBlog(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body']