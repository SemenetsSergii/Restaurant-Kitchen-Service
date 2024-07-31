from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from kitchen.models import DishType, Dish

# Define URLs for the tests
DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")
COOK_LIST_URL = reverse("kitchen:cook-list")
DISH_LIST_URL = reverse("kitchen:dish-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_LIST_URL)
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 302)  # Redirect to login page


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Jain",
            password="Tesy123456",
        )
        self.client.force_login(self.user)
        self.dish_type1 = DishType.objects.create(name="BBQ")
        self.dish_type2 = DishType.objects.create(name="Drink's")

    def test_retrieve_dish_types(self):
        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(list(
            response.context["dish-type-list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_search_dish_type(self):
        response = self.client.get(DISH_TYPE_LIST_URL, {"name": "BBQ"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BBQ")
        self.assertNotContains(response, "Drink's")


class PublicCookTest(TestCase):
    def test_login_required(self):
        response = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)  # Redirect to login page


class PrivateCookListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="User",
            password="userpass123",
        )
        self.client.force_login(self.user)
        self.cook1 = get_user_model().objects.create_user(
            username="Michael", password="password1"
        )
        self.cook2 = get_user_model().objects.create_user(
            username="Kimmi", password="password2"
        )

    def test_retrieve_cooks(self):
        response = self.client.get(COOK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        cooks = get_user_model().objects.all()
        self.assertEqual(list(response.context["cook-list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_search_cook(self):
        response = self.client.get(COOK_LIST_URL, {"username": "Michael"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Michael")
        self.assertNotContains(response, "Kimmi")


class PublicDishTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 302)  # Redirect to login page


class PrivateDishListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="User",
            password="userpass123",
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name="Appetizer")
        self.dish1 = Dish.objects.create(
            name="Snakes",
            description="A tasty dish",
            price="10.00",
            dish_type=self.dish_type,
        )
        self.dish2 = Dish.objects.create(
            name="Gold Eagle",
            description="Another tasty dish",
            price="15.00",
            dish_type=self.dish_type,
        )

    def test_retrieve_dishes(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish-list"]), list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
