from . import views
from .views import ListEmployeeAPIView,CreateEmployeeAPIView,UpdateEmployeeAPIView,DeleteEmployeeAPIView,ListEmployeeGenericAPIView,CreateEmployeeGenericAPIView,UpdateEmployeeGenericAPIView,CreateEmployeeGenericAPIViewMixin,ListEmployeeGenericAPIViewMixin,UpdateEmployeeGenericAPIView,RetrieveSingleEmployeeGenericAPIView,DeleteSingleEmployeeGenericAPIView,EmployeeListAPIView,EmployeeRetriveAPIView,EmployeeUpdateAPIView,EmployeeDeleteAPIView,EmployeeListCreateAPIView,EmployeeRetrieveUpdateAPIView,EmployeeRetrieveDestroyAPIView,EmployeeViewSet,EmployeeGenericAPIViewSet,EmployeeReadOnlyViewSet,EmployeeModelViewSet,ListDepartmentAPIView
from django.urls import path


    # 7.ViewSets Urls Started
employee_list = EmployeeViewSet.as_view({'get': 'list','post': 'create'})
employee_detail = EmployeeViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'})
    # view Set Urls End
    # GenericViewSetAPi
genericapi_employee_detail = EmployeeGenericAPIViewSet.as_view({'get': 'list'})
# EmployeeReadOnlyViewSet
readonly_employee_detail = EmployeeReadOnlyViewSet.as_view({'get': 'list'})
modelviewset_employee_list = EmployeeModelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

modelviewset_employee_detail = EmployeeModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    # 1.Function Based API Urls.
    path('function_based_api_employee_list/',views.employee_list,name='employee_list'),
    path('function_based_api_add_employee/',views.add_employee,name='add_employee'),
    path('function_based_api_add_department/',views.add_department,name='add_department'),
    path('function_based_api_update_employee/',views.update_employee,name='update_employee'),
    path('function_based_api_delete_employee/',views.delete_employee,name='delete_employee'),
    
    # 2.Function Based Api With using Serializer
    path('function_based_api_with_serializer_list_employee/',views.get_list_using_serializer,name='get_list_employee'),
    path('function_based_api_with_serializer_employee_insert_employee/',views.create_employee_using_serializer,name='create_employee_serializer'),
    path('function_based_api_with_serializer_employee_update_employee/',views.update_employee_using_serializer,name='update_employee_serializer'),
    #path('function_based_api_with_serializer_employee_delete_employee/',views.delete_employee_using_serializer,name='delete_employee_serializer'),


    #.3.Class Based API View
    path('get_all_data_using_class_based_api_view/',ListEmployeeAPIView.as_view(),name="get_all_employee"),
    path('add_employee_data_using_class_based_api_view/',CreateEmployeeAPIView.as_view(),name="create_employee_data"),
    path('update_employee_data_using_class_based_api_view/',UpdateEmployeeAPIView.as_view(),name="create_employee_data"),
    path('delete_employee_data_using_class_based_api_view/',DeleteEmployeeAPIView.as_view(),name="delete_employee_api"),

    #4.Generic api view
    path('get_all_data_using_class_based_generic_api_view/',ListEmployeeGenericAPIView.as_view(),name="get_all_employee"),
    path('add_employee_data_using_class_based_generic_api_view/',CreateEmployeeGenericAPIView.as_view(),name="create_employee_data"),
    path('update_employee_data_using_class_based_generic_api_view/<int:pk>/',UpdateEmployeeGenericAPIView.as_view(),name='update_employee_data'),

    # 5.Generic api view with Mixin
    path('add_employee_data_using_class_based_generic_api_and_mixin_view/',CreateEmployeeGenericAPIViewMixin.as_view(),name="create_employee_mixin"),
    path('list_employee_data_using_class_based_generic_api_and_mixin_view/',ListEmployeeGenericAPIViewMixin.as_view(),name="list_employee_mixin"),
    path('update_employee_data_using_class_based_generic_api_and_mixin_view/<int:pk>/',UpdateEmployeeGenericAPIView.as_view(),name="list_employee_mixin"),
    path('retrieve_single_employee_data_using_class_based_generic_api_and_mixin_view/<int:pk>/',RetrieveSingleEmployeeGenericAPIView.as_view(),name="retrieve_employee_mixin"),
    path('delete_single_employee_data_using_class_based_generic_api_and_mixin_view/<int:pk>/',DeleteSingleEmployeeGenericAPIView.as_view(),name="retrieve_employee_mixin"),

    # 6.Concrete Generic api view with Mixin
    path('add_employee_data_using_class_based_concrete_generic_api_view/',CreateEmployeeGenericAPIViewMixin.as_view(),name="create_employee_mixin"),
    path('list_employee_data_using_class_based_concrete_generic_api_view/',EmployeeListAPIView.as_view(),name="list_employee_mixin"),
    path('retrive_employee_data_using_class_based_concrete_generic_api_view/<int:pk>/',EmployeeRetriveAPIView.as_view(),name="retrive_employee_mixin"),
    path('update_employee_data_using_class_based_concrete_generic_api_view/<int:pk>/',EmployeeUpdateAPIView.as_view(),name="update_employee_generic_api"),
    path('delete_employee_data_using_class_based_concrete_generic_api_view/<int:pk>/',EmployeeDeleteAPIView.as_view(),name="delete_employee_generic_api"),
    # 2 operations in 1 api only
     # GET All, POST Create
    path('get_create_employee_data_using_class_based_concrete_generic_api_view/',EmployeeListCreateAPIView.as_view(),name='list_create_employee'),
    # GET One, PUT, PATCH
    path('retrieve_update_employee_data_using_class_based_concrete_generic_api_view/<int:pk>/',EmployeeRetrieveUpdateAPIView.as_view(),name='retrieve_update_employee'),
    # GET One, DELETE
    path('retrieve_delete_employee_data_using_class_based_concrete_generic_api_view/<int:pk>/',EmployeeRetrieveDestroyAPIView.as_view(),name='retrieve_delete_employee'),

    # 7.View Set APi
    path('employees/', employee_list),
    path('employees/<int:pk>/', employee_detail),
    path('genericapiviewset_employees/',genericapi_employee_detail),
    path('readonly_employee_detail/',readonly_employee_detail),
    path('modelviewset_employees/',modelviewset_employee_list,name='modelviewset_employee_list'),
    path('modelviewset_employees/<int:pk>/',modelviewset_employee_detail,name='modelviewset_employee_detail'),
# Department
    path(
    'get_all_departments/',
    views.ListDepartmentAPIView.as_view(),
    name='all_departments'
)

]

