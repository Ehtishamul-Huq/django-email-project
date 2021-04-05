from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from userproject.serializers import ProjectSerializer, GetProjectSerializer, ExperienceSerializer, EducationSerializer
from userproject.models import Project, Education
from user.models import User
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
class ProjectView(CreateAPIView):
    serializer_class = ProjectSerializer
    def post(self,request):
        #import pdb;pdb.set_trace()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_uuid = serializer.data['id']
        return Response({'id': user_uuid, 'data': serializer.data, 'success': 'Project has been added'}, status=status.HTTP_200_OK)



class EducationView(APIView):
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        _data = {**request.data, **{"user":request.user.pk}}
        serializer = self.serializer_class(data=_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response({'data': serializer.data,
                             'message': 'Education has been added'}, status=status.HTTP_200_OK)

    def get(self,request):
        data = Education.objects.filter(user=request.user)
        serializer = EducationSerializer(data, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class EducationUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EducationSerializer

    def get(self, request, pk):
        data = Education.objects.get(id=pk)
        if data.user == request.user:
            serializer = EducationSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):

        data = Education.objects.get(id=pk)
        if data.user == request.user:
            serializer = EducationSerializer(instance=data, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        data = Education.objects.get(id=pk)
        if data.user == request.user:
            data.delete()
            return Response({'Message': 'Education is deleted'}, status=status.HTTP_200_OK)
        return Response({'Message' : 'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)