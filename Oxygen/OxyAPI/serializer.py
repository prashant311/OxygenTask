from rest_framework import serializers
from .models import OxygenModel


class OxygenSerializer(serializers.ModelSerializer):

    class Meta:
        model = OxygenModel
        fields = ['address', 'businessName', 'personName', 'contact', 'verifiedStatus', 'timeStamp']

