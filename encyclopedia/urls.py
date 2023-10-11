from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('edit/<str:title>/', views.edit, name='edit'),
    path("save",views.save,name="save"),
    path("random",views.randomm,name="random"),
    path('createpage', views.createpage, name='createpage'),
    path("create",views.create,name="create"),
    path('search', views.search_results, name='search_results'),
    path("<str:title>",views.get,name="title"),
    path('edit/<str:title>/', views.edit, name='edit')
]
