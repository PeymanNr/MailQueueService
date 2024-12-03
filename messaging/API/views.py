from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from messaging.API.serializers import EmailSerializer


class EmailAPIView(APIView):
    def post(self, request):

        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Ok')
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
