from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from account.models import Account
from bookapp.models import Booking, Room
from bookapp.api.serializers import BookingSerializer, RoomSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

def apiOverView(request):
    return JsonResponse("API BASE POINT", safe=False)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def api_create_book_view(request):
    account = request.user
    booking = Booking(user=account)

    if request.method == "POST":
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_detail_book_view(request, bookid):
    user = request.user.username
    try:
        booking = Booking.objects.get(pk=bookid)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if booking.user.username != user:
        return Response({'response':"You don't have permission to edit that."}) 
    if request.method == 'GET':
        serializer = BookingSerializer(booking)
        return Response(serializer.data)



@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def api_update_book_view(request, bookid):
    user = request.user.username

    try:
        booking = Booking.objects.get(pk=bookid)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if booking.user.username != user:
	    return Response({'response':"You don't have permission to edit that."}) 
    
    if request.method == 'PUT':
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = UPDATE_SUCCESS
            data['pk'] = booking.pk
            data['room'] =  serializer.data['room']
            data['start_date'] = booking.start_date
            data['end_date'] = booking.end_date
            return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET',])
# @permission_classes((IsAuthenticated,))
# def api_is_author_of_blogpost(request, slug):
# 	try:
# 		blog_post = BlogPost.objects.get(slug=slug)
# 	except BlogPost.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	data = {}
# 	user = request.user
# 	if blog_post.author != user:
# 		data['response'] = "You don't have permission to edit that."
# 		return Response(data=data)
# 	data['response'] = "You have permission to edit that."
# 	return Response(data=data)


# @api_view(['DELETE',])
# @permission_classes((IsAuthenticated, ))
# def api_delete_blog_view(request, slug):

# 	try:
# 		blog_post = BlogPost.objects.get(slug=slug)
# 	except BlogPost.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	user = request.user
# 	if blog_post.author != user:
# 		return Response({'response':"You don't have permission to delete that."}) 

# 	if request.method == 'DELETE':
# 		operation = blog_post.delete()
# 		data = {}
# 		if operation:
# 			data['response'] = DELETE_SUCCESS
# 		return Response(data=data)

@api_view(['GET', 'POST, '])
def room_list_view(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
