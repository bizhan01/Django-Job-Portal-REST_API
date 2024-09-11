from rest_framework import serializers
from .models import application,candidate
from accounts import models
from django.contrib.auth import get_user_model
    

class applicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = application
        fields = "__all__"
        read_only_fields = ('id',)

class candidateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = candidate
        fields = "__all__"
        read_only_fields = ('id',)

class CandidateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','name','password')
        extra_kwargs  = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
            instance.save()
            return instance