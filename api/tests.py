from django.test import TestCase, Client
from .models import application,candidate
from rest_framework import status

client = Client()
class applicationTest(TestCase):
    def setUp(self):
        application.objects.create(position="SDE",description="Created Job",job_type="fulltime",salary="100",experience="3",location="remote")
    def testapplicationcreated(self):
        response = client.get("/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
