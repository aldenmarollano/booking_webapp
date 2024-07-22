from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from account.api.serializers import RegistrationSerializer
from account.models import Account


@api_view(['POST'],)
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data = {
                'response': "Successfully registered user.",
                'email': account.email,
                'username': account.username
            }
        else:
            data = serializer.errors

        return Response(data)
