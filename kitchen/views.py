from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import (
    Cook,
    Dish,
    DishType
)


def index(request: HttpRequest) -> HttpResponse:
    num_dish = Dish.objects.count()
    num_cook = Cook.objects.count()
    num_dish_type = DishType.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        'num_dish': num_dish,
        'num_cook': num_cook,
        "num_Dish_type": num_dish_type,
        "num_visits": num_visits,
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_types")
    template_name = "kitchen/dish_list.html"
    context_object_name = "dish_list"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")
    template_name = "kitchen/cook_list.html"
