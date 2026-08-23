from django.urls import path
from . import views
from .views import GetAllDepartmentsAPIView,GetAllDepartmentsGenericAPIView,GetAllDeptGenericAPIandModelMixin,GetallDeptGenericAPIandListApiView,GetallDeptViewset

department_list=GetallDeptViewset.as_view({'get': 'list'})
urlpatterns = [
    # 1.Function Based APIView without Serializer
    path('get_all_departments/',views.getalldepartments,name="get_all_departments"),
    # 2.Function Based APIView with Serializer
    path('get_all_departments_fbv/',views.getalldatausingfunction,name="get_all_departments_fbv"),
    # 3.Class Based APIView
    path('get_all_departments_using_class_api/',GetAllDepartmentsAPIView.as_view(),name="class_apiview"),
    # 4.GenericAPIView Based
    path('get_all_dept_using_genericapi/',GetAllDepartmentsGenericAPIView.as_view(),name="genapiview_api"),
    # 5.GenericAPIView With ModelMixins
    path('get_all_dept_genericapimixins/',GetAllDeptGenericAPIandModelMixin.as_view(),name="genericapiwithmodelmixin"),
    # 6.Concretegeneric api view
    path('get_all_dept_concretegenericapiview/',GetallDeptGenericAPIandListApiView.as_view(),name="GetallDeptGenericAPIandListApiView"),
    # 7.ViewSetAPI
    
    path('department_list_as_viewset/',department_list)
]