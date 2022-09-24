from gzip import READ
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from haberler.models import Makele
from .serializers import MakeleSerializer

# class views
from rest_framework.views import APIView



class MakaleListAPIView(APIView):
    def get(self, request):
        makaleler = Makele.objects.filter(is_active=True)
        serializer = MakeleSerializer(makaleler, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = MakeleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class MakeleDetailAPIView(APIView):





#? """ Function base views """
# @api_view(["GET", "POST"])
# def makale_list_create_view(request):

#     if request.method == "GET":
#         makaleler = Makele.objects.filter(is_active=True)
#         serializer = MakeleSerializer(makaleler, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = MakeleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def makale_detail_api_view(request, pk):
    try:
        makale_instance = Makele.objects.get(pk=pk)
    except Makele.DoesNotExist:
        return Response(
            {
                'errors': {
                    'code': 404,
                    'message': f'id ({pk}) does not exist. !!!'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serializer = MakeleSerializer(makale_instance)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MakeleSerializer(makale_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        makale_instance.delete()
        return Response(
            {
                'islem': {
                    'code': 204,
                    'message': f'id ({pk}) deleted. !!!'
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )
