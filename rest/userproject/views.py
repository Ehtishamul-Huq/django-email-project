from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from userproject.serializers import ProjectSerializer, ExperienceSerializer, EducationSerializer
from userproject.models import Project, Education, Experience

class ProjectView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        _data = {**request.data, **{"user":request.user.pk}}
        serializer = self.serializer_class(data=_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response({'data': serializer.data,
                             'message': 'Project has been added'}, status=status.HTTP_200_OK)

    def get(self,request):
        data = Project.objects.filter(user=request.user)
        serializer = ProjectSerializer(data, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class ProjectUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get(self, request, pk):
        data = Project.objects.get(id=pk)
        if data.user == request.user:
            serializer = ProjectSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = Project.objects.get(id=pk)
        if data.user == request.user:
            serializer = ProjectSerializer(instance=data, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        data = Project.objects.get(id=pk)
        if data.user == request.user:
            data.delete()
            return Response({'Message': 'Project is deleted'}, status=status.HTTP_200_OK)
        return Response({'Message' : 'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)



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


class ExperienceView(APIView):
    serializer_class = ExperienceSerializer
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        _data = {**request.data, **{"user":request.user.pk}}
        serializer = self.serializer_class(data=_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response({'data': serializer.data,
                             'message': 'Experience has been added'}, status=status.HTTP_200_OK)

    def get(self,request):
        data = Experience.objects.filter(user=request.user)
        serializer = ExperienceSerializer(data, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class ExperienceUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExperienceSerializer

    def get(self, request, pk):
        data = Experience.objects.get(id=pk)
        if data.user == request.user:
            serializer = ExperienceSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):

        data = Experience.objects.get(id=pk)
        if data.user == request.user:
            serializer = ExperienceSerializer(instance=data, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        data = Experience.objects.get(id=pk)
        if data.user == request.user:
            data.delete()
            return Response({'Message': 'Experience is deleted'}, status=status.HTTP_200_OK)
        return Response({'Message' : 'Invalid token or id'}, status=status.HTTP_400_BAD_REQUEST)

