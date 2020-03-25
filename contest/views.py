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
        except ClassContest.BadRequest:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
