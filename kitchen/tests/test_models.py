from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelTests(TestCase):
    def setUp(self) -> None:
        self.dish_type = DishType.objects.create(
            name="BBQ",
        )
        self.cook = get_user_model().objects.create(
            username="user",
            password="userpass123",
            first_name="Ecto",
            last_name="Francolin",
            years_of_experience=10,
        )

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), "BBQ")

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "user (Ecto Francolin)")

    def test_dish_str(self):
        dish = Dish.objects.create(
            name="Potato",
            description="A delicious potato dish",
            price="5.00",
            dish_type=self.dish_type,
        )
        self.assertEqual(str(dish), "Potato")

    def test_create_cook_with_years_of_experience(self):
        self.assertEqual(self.cook.years_of_experience, 10)
