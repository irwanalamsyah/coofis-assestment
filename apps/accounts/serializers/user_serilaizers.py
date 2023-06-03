from apps.accounts.models import User
from rest_framework import serializers
from django.utils import timezone

class UserRetrieveSerilaizer(serializers.ModelSerializer):
    last_login = serializers.SerializerMethodField()
    date_joined = serializers.SerializerMethodField()

    def get_last_login(self, obj):
        date = timezone.localtime(obj.last_login)
        formatted_date = date.strftime("%d %B %Y %H:%M:%S")
        return formatted_date

    def get_date_joined(self, obj):
        date = timezone.localtime(obj.date_joined)
        formatted_date = date.strftime("%d %B %Y %H:%M:%S")
        return formatted_date
    
    class Meta:
        model = User
        fields = [
            "id",
            "nip",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined"
        ]