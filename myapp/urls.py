from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('add/', views.add, name="add"),
    path('add/addRecord/', views.addRecord, name="addRecord"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    path('update/updateRecord/<int:id>',
         views.updateRecord, name="updateRecord"),

    # Authentication Routes
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout")
]
