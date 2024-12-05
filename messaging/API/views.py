from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from messaging.API.serializers import EmailSerializer
from messaging.tasks import send_email_async


class EmailAPIView(APIView):
    def post(self, request):

        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.save()
            send_email_async.delay(email.id)

            return Response('Email is being sent',
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
