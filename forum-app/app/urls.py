from django.urls import path
from . import views  # from current folder


urlpatterns = [
    path('', views.index, name="index"),

    # path('add_user', views.add_user, name="add_user"),
    # path('<int:user_id>/', views.user_detail, name="user_detail"),
    path('add_post', views.add_post, name="add_post"),

    path('<int:post_id>/', views.post_detail, name="post_detail"),
    path('<int:post_id>/add_comment', views.add_comment, name="add_comment"),
]
