from apirestappserver.models import User,UsersGroups,Categories,Membership,Classification,Rooms,Messages
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','gender','is_active','is_staff','is_superuser','date_joined','birth_date','adress','city','country','image_url']

class UsersGroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsersGroups
        fields = ['name','description','image_url','created_at','owner','members']

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['name','description']

class MembershipsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        fields = ['user','group','date_joined','invite_reason']

class ClassificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classification
        fields = ['category','group']

class RoomsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rooms
        fields = ['name','description','image_url','created_at','updated_at','group','owner']

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ['owner','room','content','created_at','updated_at']
