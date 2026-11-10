
from django import forms
from .models import Post,Subreddits, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subreddits','title', 'content', 'url', 'image']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'Title'}),
            'content':forms.Textarea(attrs={'placeholder' : 'Text(Optional)'}),
            'url':forms.URLInput(attrs={'placeholder': 'URL(optional)'})
        }

class SubredditForm(forms.ModelForm):
    class Meta:
        model = Subreddits
        fields = ['name', 'slug', 'description']
        widgets = {
                    'name':forms.TextInput(attrs={'placeholder':'Name of Subreddit'}),
                    'slug':forms.Textarea(attrs={'placeholder' : 'Slug'}),
                    'description':forms.Textarea(attrs={'placeholder': 'Description(optional)'})
                }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
        widgets = {
            'content' : forms.Textarea(attrs={'placeholder': 'To reply to a comment, \nadd the name of author'})
        }