from django import forms
from taggit.forms import TagWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={
                'placeholder': 'Add tags separated by commas',
                'class': 'tag-input',
                'data-tagify': 'true'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here'
            })
        }
        help_texts = {
            'tags': 'Separate tags with commas'
        }

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', [])
        if len(tags) > 5:
            raise forms.ValidationError("You can't add more than 5 tags.")
        return tags