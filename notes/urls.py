from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_notes, name="login"),
    path('logout/', views.logout_notes, name="logout"),
    path('register/', views.register_notes, name="register"),
    path('notes/', views.notes, name="notes"),
    path('view-notes/<str:pk>/', views.view_notes, name="view-notes"),
    path('add-notes/', views.add_notes, name="add-notes"),
    path('update-notes/<str:pk>/', views.update_notes, name="update-notes"),
    path('delete-notes/<str:pk>/', views.delete_notes, name="delete-notes"),
    path('user-page/', views.user_page, name="user-page"),

]