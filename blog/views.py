from .models import  Perro
from rest_framework import viewsets
# from blog.serializers import PostSerializer
from blog.serializers import PerroSerializer

# class PostViewSet( viewsets.ModelViewSet ):
#     queryset = Post.objects.all().order_by( 'published_date')
#     serializer_class = PostSerializer

class PerroViewSet( viewsets.ModelViewSet ):
    queryset = Perro.objects.all().order_by( 'name' )
    serializer_class = PerroSerializer