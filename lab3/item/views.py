from django.shortcuts import render
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from .serializer import ItemSerializer
from .models import Item
from rest_framework.generics import get_object_or_404

# Create your views here.
class ItemView(views.APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"items": serializer.data})

class ItemCreateView(views.APIView):
    def post(self, request):
        item = request.data

        serializer = ItemSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()

        return Response({"POST success": "Item {} created successfully".format(item_saved.name)})

class ItemUpdateView(views.APIView):
    def put(self, request, pk):
        try:
            item_with_pk =  Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        serializer = ItemSerializer(instance=item_with_pk, data=data, partial=False)
        if serializer.is_valid():
            item_saved = serializer.save()

        return Response({"PUT success": "Item with id {} was updated successfully".format(pk)})

    def patch(self, request, pk):
        try:
            item_with_pk = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        serializer = ItemSerializer(instance=item_with_pk, data=data, partial=True)
        if serializer.is_valid():
            item_saved = serializer.save()

        return Response({" PATCH success": "Item with id {} was updated successfully".format(pk)})