from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Organization, Otdel, Sotrudnik
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget
from django.urls import reverse_lazy


class OrganizationForm(forms.ModelForm):

    # tags = TagField(required=False, widget=LabelWidget)

    class Meta:
        model = Organization
        # fields = []
        exclude = []

    # def clean(self):
    #     cleaned_data = super().clean()
    #     slug = cleaned_data.get("alias")

    #     try:
    #         post = Post.objects.get(alias=slug)
    #     except Post.DoesNotExist:
    #         post = None

    #     if post:
    #         msg = "Пост с alias \"{}\" - уже существует".format(slug)
    #         self.add_error("alias", msg)

class OtdelForm(forms.ModelForm):
    class Meta:
        model = Otdel
        # fields = []
        exclude = []


class SotrudnikForm(forms.ModelForm):

    # organization = forms.CharField(widget=forms.Select(attrs={"data-otdels-url": reverse("get-otdels", kwargs={"org_id": 1})}))
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        #   widget=forms.Select(attrs={"data-otdels-url": "/"}))

        # передаем в атрибут формы url для дальнейшей загрузки данных поля "otdel" через js
        # org_id=1 вставлен для того чтобы сработал reverse, далее будет отрезан в js
        widget=forms.Select(
            attrs={"data-otdels-url": reverse_lazy("get-otdels")}
        )
    )

    class Meta:
        model = Sotrudnik
        # fields = []
        exclude = []

    class Media:
        js = ('structure/js/sotrudnik_form.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # assert False, reverse_lazy("get-otdels-for-org", kwargs={"org_id": 1})[:-1]
        self.fields['otdel'].queryset = Otdel.objects.none()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     organization = cleaned_data.get("organization")
    #     otdel = cleaned_data.get("otdel")

    #     if organization and otdel:
    #         assert False, (organization, otdel)
    #         msg = "Пост с alias \"{}\" - уже существует".format(slug)
    #         self.add_error("alias", msg)
