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

    def clean(self):
        cleaned_data = super().clean()
        slug = cleaned_data.get("alias")

        try:
            Post.objects.get(alias=slug)
        except Post.DoesNotExist:
            msg = "Пост с таким \"alias\" уже существует"
            self.add_error("alias", msg)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = []
        exclude = []