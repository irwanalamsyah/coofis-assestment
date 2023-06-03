from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from apps.accounts.serializers.user_serilaizers import UserRetrieveSerilaizer
from rest_framework.response import Response

from apps.common.utils import set_response_message

class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserRetrieveSerilaizer

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        set_response_message(self, message="data found")
        return Response(serializer.data, status=status.HTTP_200_OK)
