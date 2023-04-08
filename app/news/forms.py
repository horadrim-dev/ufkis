from django import forms
from .models import Post, Category
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget


class PostForm(forms.ModelForm):

    tags = TagField(required=False, widget=LabelWidget)

    class Meta:
        model = Post
        # fields = []
        exclude = []


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = []
        exclude = []