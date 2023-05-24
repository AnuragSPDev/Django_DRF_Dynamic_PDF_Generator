from django.urls import path
from . import views

urlpatterns = [
    path('list_view/', views.EmployeeListView.as_view(), name='list_view'),
    path('pdf_generator_view/', views.EmployeeGeneratePdfAPIView.as_view(), name='pdf_generator_view'),
]
