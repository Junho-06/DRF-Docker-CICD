from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        idf = User.objects.filter(idf=attrs['idf'])
        if idf.exists():
            raise serializers.ValidationError('이 아이디는 이미 존재합니다.')
        return attrs