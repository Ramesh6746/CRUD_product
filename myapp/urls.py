from django.urls import path
from.import views

urlpatterns = [
    path('Addstudent/',views.student,name='home')
]