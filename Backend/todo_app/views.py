from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer,TaskCreateSerializer
from rest_framework import status


# Create your views here.


class TaskListView(APIView):
        def get(self,request):
            try:
                task = Task.objects.all()
                serializer = TaskSerializer(task,many=True)
                return Response(serializer.data)
            except:
                    return Response({'msg':'Task not found'})



class TaskDetailsView(APIView):
      def get(self,request,pk):
            try:
                task = Task.objects.get(id=pk)
                serializer = TaskSerializer(task,many=False)  
                return Response(serializer.data)
            except:
                  return Response({'msg':'Task details not found'})
                  

class TaskCreateView(APIView):
      def post(self,request):
            data = request.data
            serializer = TaskCreateSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer.save()
                  return Response({'msg':'Task created successfully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      


class TaskUpdateView(APIView):
        def post(self,request,pk):
            try:
                task = Task.objects.get(id=pk)
                serializer = TaskSerializer(instance=task,data=request.data)
                if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response({'msg':'task updated'},serializer.data,status=status.HTTP_200_OK)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return Response({'msg': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                  

class TaskDeleteView(APIView):
      def delete(self,request,pk):
            try:
                task = Task.objects.get(id=pk)
                task.delete()
                return Response({'msg':'Task deleted successfully'},status=status.HTTP_204_NO_CONTENT)
            except Task.DoesNotExist:
                  return Response({'msg':'Task not found'},status=status.HTTP_404_NOT_FOUND)
                  