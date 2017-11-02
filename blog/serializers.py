
from rest_framework import serializers

from blog.models import Login, Consumer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Consumer
        fields = ('url', 'UserName', 'Email','Password')
