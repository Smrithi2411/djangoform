from django.urls import path

from studentapp import views

urlpatterns = [
    path('', views.StudentView.as_view(), name="add-contact"),
    path('list/', views.ContactListView.as_view(), name="list-contact"),
    path('update/<id>/', views.ContactUpdateView.as_view(), name="update-contact"),

]