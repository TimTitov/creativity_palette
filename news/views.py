from rest_framework.response import Response
from .models import News, ImageModel, Contest, FeedFile
from .serializers import NewsSerializer, ImageSerializer, ConrestSerializer, FileSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def get_all_news(request):
    # try:
    #     news = News.objects.all()
    # except News.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
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





@api_view(['GET'])
def get_all_image(request):
    # try:
    #     news = News.objects.all()
    # except News.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        image = ImageModel.objects.all()
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



@api_view(['GET'])
def get_all_contest(request):
    # try:
    #     news = News.objects.all()
    # except News.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        con = Contest.objects.all()

        serializer = ConrestSerializer(con, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_contest(request):
    # try:
    #     news = News.objects.all()
    # except News.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        id = int(request.GET.get("id"))
        con = Contest.objects.filter(id=id)
        #[{i.file} for i in FeedFile.objects.filter(feed=con[0].id)]
        con[0].сontest_files = [i for i in FeedFile.objects.filter(feed=con[0].id)]
        print([i for i in FeedFile.objects.filter(file='files/2020/03/24/laba_10.docx')])
        print(con[0].сontest_files)
        serializer = ConrestSerializer(con, many=True)
        #print(serializer)
        return Response(serializer.data)

@api_view(['GET'])
def get_file(request):
    if request.method == 'GET':
        id = int(request.GET.get("id"))
        print([i.file for i in FeedFile.objects.filter(feed=id)])

        f = FeedFile.objects.filter(feed=id)


        serializer =FileSerializer(f, many=True)
        return Response(serializer.data)

# @api_view(['POST'])
# def add_news(request):
#     if request.method == 'POST':
#
#         serializer = FileSerializer(data=request.data)
#         id = int(request.GET.get("id"))
#         print([i.file for i in FeedFile.objects.filter(feed=id)])
#
#         f = FeedFile.objects.filter(feed=id)
#
#
#         serializer =FileSerializer(f, many=True)
#         return Response(serializer.data)
#
# @api_view(['POST'])
# def add_news(request):
#     if request.method == 'POST':
#         serializer = NewsSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)