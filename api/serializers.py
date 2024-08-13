from rest_framework import serializers
from .models import *

class BlogInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogInfo
        fields = ['id', 'title', 'description', 'published_date']