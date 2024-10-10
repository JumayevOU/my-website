from django.urls import path
from .views import indexView, blogView, detailView, commentView

urlpatterns = [
    path('', indexView, name='index'),
    path('blog/', blogView, name='blog'),
    path('blog/<int:pk>/', detailView, name='detail'),
    path('comment/<int:pk>/', commentView, name='comment'),
  

]

