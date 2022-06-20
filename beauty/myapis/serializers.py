from .models import Hero, Villian
from rest_framework import serializers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias', 'super_power')


class VillianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villian
        fields = ('id','name', 'alias', 'super_power', 'against')
