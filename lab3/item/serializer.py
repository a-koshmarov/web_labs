from rest_framework import  serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

        def create(self, validated_data):
            return Item.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.price = validated_data.get('price', instance.price)

            instance.save()
            return instance