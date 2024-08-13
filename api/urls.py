from django.urls import path
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/', views.blog_list),
    path('api/<int:id>', views.blog_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)