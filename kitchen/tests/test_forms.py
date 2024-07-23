from django.test import TestCase

from kitchen.forms import (
    CookCreateForm,
    CookSearchForm,
    CookYearUpdateForm,
    DishSearchForm,
    DishTypeSearchForm,
)
from kitchen.models import Cook, Dish, DishType


class CookCreateFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            "username": "user",
            "password1": "userpass123",
            "password2": "userpass123",
            "first_name": "Yannick ",
            "last_name": "Alleno",
            "years_of_experience": 25,
        }

    def test_valid_form(self):
        form = CookCreateForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience(self):
        # Test with years_of_experience > 99
        form = CookYearUpdateForm(
            data={**self.valid_data, "years_of_experience": 100}
        )
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)

        # Test with years_of_experience < 0
        form = CookYearUpdateForm(
            data={**self.valid_data, "years_of_experience": -1}
        )
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)

    def test_password_mismatch(self):
        form = CookCreateForm(
            data={**self.valid_data, "password2": "differentpass"}
        )
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_form_initialization(self):
        form = CookCreateForm()
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("years_of_experience", form.fields)


class CookSearchFormTests(TestCase):
    def test_valid_search(self):
        form = CookSearchForm(data={"username": "Yannick"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "Yannick")

    def test_empty_search(self):
        form = CookSearchForm(data={"username": ""})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "")


class DishSearchFormTests(TestCase):
    def test_valid_search(self):
        form = DishSearchForm(data={"name": "Pasta alla carbonara"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Pasta alla carbonara")

    def test_empty_search(self):
        form = DishSearchForm(data={"name": ""})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")


class DishTypeSearchFormTests(TestCase):
    def test_valid_search(self):
        form = DishTypeSearchForm(data={"name": "BBQ"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "BBQ")

    def test_empty_search(self):
        form = DishTypeSearchForm(data={"name": ""})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")
