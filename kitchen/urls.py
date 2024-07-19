from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishTypeCreateView,
    DishCreateView,
    DishTypeUpdateView,
    DishUpdateView,
    DishTypeDeleteView,
    DishDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),


    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),

    path("cook/", CookListView.as_view(), name="cook-list"),

]

app_name = "kitchen"
