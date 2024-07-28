from django.urls import path

from kitchen.views import (
    index,

    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishTypeDetailView,

    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,

    CookListView,
    CookCreateView,
    CookDeleteView,
    CookUpdateView,
    CookDetailView,

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "dish-types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "dishs/", DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishs/create/", DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dishs/<int:pk>/update/", DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishs/<int:pk>/delete/", DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dishs/<int:pk>/", DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "cooks/", CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/", CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cooks/create/", CookCreateView.as_view(),
        name="cook-create"
    ),
    path(
        "cooks/<int:pk>/delete/", CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path(
        "cooks/<int:pk>/update/", CookUpdateView.as_view(),
        name="cook-update"
    ),
]

app_name = "kitchen"
