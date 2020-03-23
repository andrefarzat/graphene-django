from py.test import raises

from django import forms
from django.db import models

from ..forms.mutation import DjangoModelFormMutation, Field
from ..types import DjangoObjectType
from .models import Pet


# Testing: BaseDjangoFormMutation

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'age', )


class PetType(DjangoObjectType):
    class Meta:
        model = Pet


class PetMutation(DjangoModelFormMutation):
    pet = Field(PetType)

    class Meta:
        form_class = PetForm


def test_BaseDjangoFormMutation():
    kwargs = {'name': 'Name 1', 'age': -1}
    a = PetMutation(errors=[], **kwargs)
