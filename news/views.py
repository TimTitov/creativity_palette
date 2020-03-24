from rest_framework.response import Response
from .models import ClassNews, ClassImage
from .serializers import NewsSerializer, ImageSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def get_all_news(request):
    if request.method == 'GET':
        try:
            news = ClassNews.objects.all()
        except ClassNews.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_news(request):
    if request.method == 'POST':
        try:
            serializer = NewsSerializer(data=request.data)
        except ClassNews.BadRequest:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_image(request):
    # try:
    #     news = News.objects.all()
    # except News.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        image = ClassImage.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def add_news(request):
    if request.method == 'POST':
        serializer = NewsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


