from django.urls import path
from studyportal import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="home"),
    path('home/', views.home, name="home"),
    path('notes/', views.notes, name="notes"),
    path('youtube/', views.youtube, name="youtube"),
    path('todo/', views.todo, name="todo"),
    path('books/', views.books, name="books"),
    path('wiki/', views.wiki, name="wiki"),
    path('dictionary/', views.dictionary, name="dictionary"),

    path('delete_notes/<int:pk>', views.delete_notes, name="delete_notes"),
    path('delete_todo/<int:pk>', views.delete_todo, name="delete_todo"),
    path('update_todo/<int:pk>', views.update_todo, name="update_todo"),


]
