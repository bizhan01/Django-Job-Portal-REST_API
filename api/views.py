from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import application,candidate
from .serializers import applicationSerializer, candidateSerializer, CandidateUserProfileSerializer
from rest_framework import status
from accounts.models import UserProfile
import requests
import logging 




class applicationView(ModelViewSet):
    queryset = application.objects.all()
    serializer_class = applicationSerializer



class candidateView(ModelViewSet):
    queryset = candidate.objects.all()
    serializer_class = candidateSerializer


class CandidateUserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = CandidateUserProfileSerializer

