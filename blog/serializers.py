from rest_framework import serializers
from .models import Perro



class PerroSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Perro
        fields= ('id','name','estado','description','imageUrl')