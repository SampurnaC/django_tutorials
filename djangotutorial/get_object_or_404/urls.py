from django.urls import path
from .views import home, post_detail

app_name="posts"

urlpatterns = [
    path('', home, name='home'),
    path('posts/<int:pk>/', post_detail,name='post_detail')

]
