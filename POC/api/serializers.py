from rest_framework import serializers

from POC.models import Registration

class POCSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=['id','name','age','gender','country','city','zip','address']
