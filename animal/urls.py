from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list_create_view, name='get_post_movies'),
    path('<int:pk>/', views.animal_detail_view, name='get_delete_update_movie'),
]
