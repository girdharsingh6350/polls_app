from django.urls import path
from . import views


app_name = 'Polls'
urlpatterns = [
    path('home',views.signup,name='home'),
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='DetailView'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    
]