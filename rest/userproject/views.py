from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from userproject.serializers import ProjectSerializer, GetProjectSerializer, ExperienceSerializer, EducationSerializer
from userproject.models import Project
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
class ProjectView(CreateAPIView):
    serializer_class = ProjectSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        user_uuid = serializer.data['id']

        return Response({'id': user_uuid, 'data': serializer.data, 'success': 'Project has been added'}, status=status.HTTP_200_OK)

class ExperienceView(CreateAPIView):
    serializer_class = ExperienceSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        user_uuid = serializer.data['id']
        return Response({'id': user_uuid, 'data': serializer.data, 'success': 'Experience has been added'}, status=status.HTTP_200_OK)

class EducationView(CreateAPIView):
    serializer_class = EducationSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        user_uuid = serializer.data['id']
        return Response({'id': user_uuid, 'data': serializer.data, 'success': 'Education has been added'}, status=status.HTTP_200_OK)


class GetProjectView(RetrieveAPIView):
    serializer_class = GetProjectSerializer
    def validate(self,data):
        #import pdb; pdb.set_trace()
        title = data.get("title", None)
        start_date = data.get("start_date", None)
        end_date = data.get("end_date", None)        
        if title is None:
            raise serializers.ValidationError(
                'This title is not found.'
            )
        return Response({"data": title, "start_date": start_date, "end_date": end_date}, status=status.HTTP_200_OK)

