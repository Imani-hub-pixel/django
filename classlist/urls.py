from django.urls import path
from .views import add_student_view, class_list_view
urlpatterns = [
    path('add-student/', add_student_view, name='add_student'),
    path('class-list/', class_list_view, name='class_list'),
]