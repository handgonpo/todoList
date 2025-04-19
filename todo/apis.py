from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

# generics을 위해 모듈추가
from rest_framework import generics
# from rest_framework import status, generics -> 같은 모듈안에 있으므로 합치기

# Viewsets을 위한 모듈추가
from rest_framework import viewsets
# from rest_framework import status, generics viewsets -> 같은 모듈안에 있으므로 합치기


# REST Framework_APIView
class TodoListAPI(APIView):
    
    def get(self, request):
        todos = Todo.objects.all() # QuerySet = Object list
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    

class TodoCreateAPI(APIView):

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)
    

class TodoRetrieveAPI(APIView):

    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    

class TodoUpdateAPI(APIView):

    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    

class TodoDeleteAPI(APIView):

    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# REST Framework_GenericAPIView        
class TodoGenericsListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsCreateAPI(generics.CreateAPIView):
    serializer_class = TodoSerializer


class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsUpdateAPI(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoGenericsDeleteAPI(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# Generics list + create 
class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Generics retriver + update + delete 
class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# REST Framework_ViewSets    
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer  