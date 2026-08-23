# 1.Function Based APIView Without Serializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from employee.models import Department


@csrf_exempt
def getalldepartments(request):
    print("Working file")
    all_department=Department.objects.all().values()
    serialized_data=list(all_department)
    return JsonResponse({"response":"Data Fetched Successfully...","Data":serialized_data})



# 2.Function Based APIView With Serializer
from .serializers import DepartmentSerializer
@csrf_exempt
def getalldatausingfunction(request):
    all_departments=Department.objects.all()
    serialized_data=DepartmentSerializer(all_departments,many=True)
    return JsonResponse({"response":"Data Fetched Successfully...","Data":serialized_data.data})


# 3.Class Based APIView 
from rest_framework.decorators import APIView
from rest_framework.response import Response
class GetAllDepartmentsAPIView(APIView):
    def get(self,request):
        all_departments=Department.objects.all()
        serialized_data=DepartmentSerializer(all_departments,many=True)
        return Response({"response":"Data Fetched Successfully...","Data":serialized_data.data})


# 4.Generic APIView
from rest_framework.generics import GenericAPIView
class GetAllDepartmentsGenericAPIView(GenericAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    def get(self,request):
        serialized_data=self.get_queryset()
        result=self.get_serializer(serialized_data,many=True)
        return Response({"response":"Data Fetched Successfully...","data":result.data})

# 5.GenericAPIView With Mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
class GetAllDeptGenericAPIandModelMixin(ListModelMixin,GenericAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    def get(self,request):
        return self.list(request)

# 6.concrete Generic apiview
from rest_framework.generics import ListAPIView

class GetallDeptGenericAPIandListApiView(ListAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

# 7. ViewSet Api
from rest_framework.viewsets import ViewSet

class GetallDeptViewset(ViewSet):
    def list(self,request):
        alldepartments=Department.objects.all()
        serializer=DepartmentSerializer(alldepartments,many=True)
        return Response({"response":serializer.data})