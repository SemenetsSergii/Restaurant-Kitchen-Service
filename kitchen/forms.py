from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Cook


class CookCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience")
        validated_years = validation_year_of_experience(years_of_experience)
        return validated_years


class CookYearUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience")
        validated_years = validation_year_of_experience(years_of_experience)
        return validated_years


def validation_year_of_experience(years_of_experience: int) -> int:
    if years_of_experience > 99:
        raise ValidationError(
            "The length of service should not be greater than 99 years"
        )
    elif years_of_experience < 0:
        raise ValidationError("The length of service should not be less than 0")
    return years_of_experience


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Cook"}),
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Dish"}),
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Dish Type"}),
    )
