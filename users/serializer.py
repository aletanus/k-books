from rest_framework import serializers
from users.models import Users
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Users.objects.all(), message="Email already registered")]
    )
    class Meta:
        model = Users
        fields = ['id','first_name', 'last_name','username','email', 'password', 'student', 'blocked', 'is_superuser']
        extra_kwargs = {
            'password':{'write_only': True},
            'id':{'read_only': True},
            'blocked': {'read_only': True},
            'is_superuser':{'read_only': True},
        }
    def create (self, validated_data):
        student = validated_data.pop("student", None)
        email = validated_data.get("email")
        username = validated_data.get("username")
        if Users.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'Username already registered'})
        if Users.objects.filter(email=email).exists():
           raise serializers.ValidationError({'email': 'Email already registered'})

    
        if student:
           user = Users.objects.create_user(student=True,   **validated_data)  
        else:    
           user = Users.objects.create_superuser(student=False, **validated_data)

        return user
        