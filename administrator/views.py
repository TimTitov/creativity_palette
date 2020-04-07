from rest_framework.response import Response
from .models import Administrator
from .serializers import AdministratorSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
def check_admin_or_not(request):
    if request.method == 'POST':
        try:
            login = request.data['login']
            password = request.data['password']
            serializer = AdministratorSerializer(data=request.data)
        except AdministratorSerializer.BadRequest:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            admin = Administrator.objects.get(login=login)
            if admin.password == password:
                return Response("Successful", status=status.HTTP_200_OK)
            else:
                return Response("Failed", status=status.HTTP_403_FORBIDDEN)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def admin_password_change(request):
    try:
        login = request.data['login']
        admin = Administrator.objects.get(login=login)
        old_password = request.data['old_password']
        new_password = request.data['new_password']

        if old_password == admin.password:
            adm = {
                "login": login,
                "password": new_password
            }
            serializer = AdministratorSerializer(admin, data=adm)
        if serializer.is_valid():
            serializer.save()
            return Response("Successful", status=status.HTTP_200_OK)
        else:
            return Response("Failed", status=status.HTTP_403_FORBIDDEN)

    except AdministratorSerializer.BadRequest:
        return Response(status=status.HTTP_400_BAD_REQUEST)
