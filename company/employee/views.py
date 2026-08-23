from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Employee,Department
import json
from .system_error import validate_department
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q,F

# 1.Function Based API
@csrf_exempt
def employee_list(request):
    # 1.all()
    employees=Employee.objects.filter()
    if employees:
        employees=employees.values()
        employees=list(employees)
        return JsonResponse({'message':'Data Fetched Successfully...','data':employees}, safe=False)
    return JsonResponse({'message':'Data Not Available...'}, safe=False)

@csrf_exempt
def add_employee(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            name=data.get('name')
            email=data.get('email')
            salary=data.get('salary')
            department_id=data.get('department')
            department=Department.objects.get(id=department_id)
            age=data.get('age')
            status=data.get('status')
            result=Employee.objects.create(name=name,email=email,salary=salary,department=department,age=age,status=status)
            if result:
                return JsonResponse({'message':'Employee Added successfully.....'})
            return JsonResponse({'message':'Error Adding Employee'})
    except Exception as e:
        return JsonResponse({
            'status':False,
            'message':str(e)
        })

@csrf_exempt
def add_department(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            name=data.get("name")
            validate_data=validate_department(name)
            if validate_data:
                  return JsonResponse({
                    "status": False,
                    "message": "Department name is required"
                    })
            result=Department.objects.create(name=data.get("name"))
            if result:
                return JsonResponse({"response":"Department added Successfully...."})
            return JsonResponse({"response":"Error adding Department...."})
    except Exception as e:
        return JsonResponse(
            {
                'status':False,
                'message':str(e)
            }
        )



@csrf_exempt
def update_employee(request):
    data = json.loads(request.body)
    emp_id = data.get("id")
    name = data.get("name")
    email = data.get("email")

    updated_count = Employee.objects.filter(
        id=emp_id
    ).update(
        name=name,
        email=email
    )

    if updated_count:
        return JsonResponse({
            "message": "User Details Updated Successfully..."
        })

    return JsonResponse({
        "message": "User Details Not Found..."
    })


@csrf_exempt
def delete_employee(request):
    data=json.loads(request.body)
    id=data.get("id")
    print("Type",type(id))
    result,_=Employee.objects.filter(id=id).delete()
    if result:
        return JsonResponse({"message": "User Details Deleted Successfully..."})
    
# # 1.Function Based API Using Serializer

from .serializers import EmployeeSerializer,DepartmentSerializer

@csrf_exempt
def get_list_using_serializer(request):
    data=Employee.objects.all()
    serializer=EmployeeSerializer(data,many=True)
    print(serializer.data,type(serializer.data))
    response=serializer.data
    return JsonResponse({'response':response})

@csrf_exempt
def create_employee_using_serializer(request):
    data=json.loads(request.body)
    serialier=EmployeeSerializer(data=data)
    if serialier.is_valid():
        serialier.save()
        return JsonResponse({"response":"Employee Created Successfully....."})
    return JsonResponse({"response":serialier.errors})

@csrf_exempt
def update_employee_using_serializer(request):
    data=request.body
    serialized_data=json.loads(data)
    id=serialized_data.get("id")
    existing_object=Employee.objects.get(id=id)
    serializer=EmployeeSerializer(existing_object,data=serialized_data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"response":"Employee Data Updated Successfully...."})
    return JsonResponse({"response":serializer.errors})

# serializer is not requiured in case of delete
# @csrf_exempt
# def delete_employee_using_serializer(request):
#     data=json.loads(request.body)
#     id=data.get("id")

# CREATE -> Serializer
# READ   -> Serializer
# UPDATE -> Serializer
# DELETE -> Direct delete()

# 3.Class Based API View
from rest_framework.decorators import APIView
from rest_framework.response import Response


class ListDepartmentAPIView(APIView):
    def get(self,request):
        data=Department.objects.all()
        serializer=DepartmentSerializer(data,many=True)
        response=serializer.data
        return Response({"msg":"Data fetched Successfully","response":response})
class ListEmployeeAPIView(APIView):
    def post(self,request):
        data=Employee.objects.all()
        serialize_data=EmployeeSerializer(data,many=True)
        response=serialize_data.data
        return Response({"msg":"Data fetched Successfully","response":response})
    
class CreateEmployeeAPIView(APIView):
    def post(self,request):
        data=request.data
        serializer=EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"Employee Added Successfully..."})
        return Response({"response":serializer.errors})

class UpdateEmployeeAPIView(APIView):
    def post(self,request):
        data=request.data
        id=data.get("id")
        existing_data=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(existing_data,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"Employee Updated Successfully..."})
        return Response({"response":serializer.errors})
class DeleteEmployeeAPIView(APIView):
    def post(self,request):
        data=request.data
        id=data.get("id")
        result,_=Employee.objects.filter(id=id).delete()
        if result:
            return Response({"response":"Employee Deleted Successfully..."})
        return Response({"response":"Error while deleting user"})
    

# 4.API Using Generic API View
from rest_framework.generics import GenericAPIView

class ListEmployeeGenericAPIView(GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request):
        employees=self.get_queryset()
        serializer=self.get_serializer(employees,many=True)
        return Response(serializer.data)


class CreateEmployeeGenericAPIView(GenericAPIView):
    serializer_class=EmployeeSerializer
    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"Employee Added Successfully..."})
        return Response({"response":serializer.errors})
    
class UpdateEmployeeGenericAPIView(GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,pk):
        employee=self.get_object()
        serializer=self.get_serializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"Employee Added Successfully.."})
        return Response({"response":serializer.errors})
    
# 5.API Using Generic API View With Mixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin

class CreateEmployeeGenericAPIViewMixin(CreateModelMixin,GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request):
        return self.create(request)
    
class ListEmployeeGenericAPIViewMixin(ListModelMixin,GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request):
        return self.list(request)
    
class UpdateEmployeeGenericAPIView(UpdateModelMixin,GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,pk):
        return self.update(request)
    
class RetrieveSingleEmployeeGenericAPIView(RetrieveModelMixin,GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,pk):
        return self.retrieve(request,pk=pk)
    
class DeleteSingleEmployeeGenericAPIView(DestroyModelMixin,GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,pk):
        return self.destroy(request,pk=pk)
    


# 6.Concrete Generic Views
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView

class EmployeeCreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeListAPIView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeRetriveAPIView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeDeleteAPIView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# ListCreateAPIView
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
# RetrieveUpdateAPIView
class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# RetrieveDestroyAPIView
class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# 7 ViewSet Api
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class EmployeeViewSet(ViewSet):
    def list(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def create(self, request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        employee=Employee.objects.get(pk=pk)
        serializer=EmployeeSerializer(employee,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response({"response": "Employee Deleted Successfully..."})

# 8.GenericViewSet
from rest_framework.viewsets import GenericViewSet
class EmployeeGenericAPIViewSet(GenericViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def list(self,request):
        employees=self.get_queryset()
        serializer = self.get_serializer(employees,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'response':serializer.data})
        return Response({"response":"Error while adding data"})

# 9.ReadOnlyModelViewSet

from rest_framework.viewsets import ReadOnlyModelViewSet

class EmployeeReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# 10.ModelViewSet
from rest_framework.viewsets import ModelViewSet

class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

