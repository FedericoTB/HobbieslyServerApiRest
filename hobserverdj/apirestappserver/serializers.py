from apirestappserver.models import User,UsersGroups,Categories,Membership,Classification,Rooms,Messages
from rest_framework import serializers
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','gender','birth_date','adress','city','country','image_url','password']

    def create(self, validated_data, **kwargs):
        """
        Overriding the default create method of the Model serializer.
        """
        print(validated_data)
        user = User(
            username=validated_data['username'],
            email=validated_data["email"],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            is_active=True,
            is_staff=False,
            is_superuser=False,
            date_joined=timezone.now(),
            birth_date=validated_data['birth_date'],
            adress=validated_data['adress'],
            city=validated_data['city'],
            country=validated_data['country'],
            image_url=validated_data['image_url']
        )
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(LoginSerializer, self).validate(attrs)
        # Custom data include in the response
        data.update({"id": self.user.id})
        data.update({"username": self.user.username})
        data.update({"email": self.user.email})
        data.update({"first_name": self.user.first_name})
        data.update({"last_name": self.user.last_name})
        return data

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

class UpdateUserSerializer(serializers.ModelSerializer):
    """
    Serializer to update the information of a logged-in user
    """

    class Meta:
        model = User
        fields = ('first_name','last_name','city','country','image_url')


    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.first_name=validated_data['first_name'],
        instance.last_name=validated_data['last_name'],
        instance.city=validated_data['city'],
        instance.country=validated_data['country']
        instance.image_url=validated_data['image_url']
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Change the password of the user.
    Note that the user sending the request must
    be the same user whose password is to be changed
    """

    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.set_password(validated_data["password"])
        instance.save()
        return instance

class UsersGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersGroups
        fields = ['id','name','description','image_url','created_at','owner']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','name','description']

class MembershipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id','user','group','date_joined','invite_reason']

class ClassificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ['id','category','group']

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ['id','name','description','image_url','created_at','updated_at','group','owner']

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id','owner','room','content','created_at','updated_at']
