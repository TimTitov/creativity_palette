from rest_framework.response import Response
from .models import ClassGallery
from .serializers import GallerySerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'PUT', 'DELETE'])
def gallery_detail(request, pk):
    try:
        gallery = ClassGallery.objects.get(pk=pk)
    except ClassGallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GallerySerializer(gallery)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GallerySerializer(gallery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)