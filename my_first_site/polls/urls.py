from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('question_l/', views.Question_List.as_view(), name='Question_List'),
    path('question_ru/<int:question_id>/', views.Question_Detail.as_view(), name='Question_Detail'),
    path('choice_l/', views.Choice_List.as_view(), name='Choice_List'),




]