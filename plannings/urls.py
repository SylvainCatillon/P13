from django.urls import path

from plannings import views

app_name = 'plannings'
urlpatterns = [
    path('create/', views.create_planning, name='create')
]