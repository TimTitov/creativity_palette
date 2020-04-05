from rest_framework.response import Response
from .models import ClassFile, ClassContest
from .serializers import ContestSerializer, FileSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def get_all_contest(request):
    if request.method == 'GET':
        con = ClassContest.objects.all()
        serializer = ContestSerializer(con, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_contest(request):
    if request.method == 'GET':
        id = int(request.GET.get("id"))
        con = ClassContest.objects.filter(id=id)
        con[0].сontest_files = [i for i in ClassFile.objects.filter(feed=con[0].id)]
        print([i for i in ClassFile.objects.filter(file='files/2020/03/24/laba_10.docx')])
        print(con[0].сontest_files)
        serializer = ContestSerializer(con, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_file(request):
    if request.method == 'GET':
        id = int(request.GET.get("id"))
        print([i.file for i in ClassFile.objects.filter(feed=id)])

        f = ClassFile.objects.filter(feed=id)
        serializer = FileSerializer(f, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_contest(request):
    if request.method == 'POST':
        try:
            serializer = ContestSerializer(data=request.data)
        except ContestSerializer.BadRequest:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def file_add(request, pk):
    if request.method == 'POST':
        try:
            serializer = FileSerializer(data=request.data)
        except FileSerializer.BadRequest:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def file_delete(request, pk):
    try:
        file = ClassFile.objects.get(pk=pk)
    except ClassFile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def contest_detail(request, pk):
    try:
        contests = ClassContest.objects.get(pk=pk)
    except ClassContest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContestSerializer(contests)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContestSerializer(contests, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)