
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subreddits','title', 'content', 'url', 'image']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Title'}),
            'content':forms.Textarea(attrs={'placeholder' : 'Text(Optional)'}),
            'url':forms.URLInput(attrs={'placeholder': 'URL(optional)'})
        }
