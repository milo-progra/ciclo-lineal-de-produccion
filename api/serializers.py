from rest_framework import serializers
from user.models import Usuario

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        #exclude define los campos que no apareceran en la consulta
        #exclude = ['user_permissions', 'groups', 'is_active', 'date_joined', 'is_superuser']
        fields = 'first_name', 'last_name', 'email', 'telefono'