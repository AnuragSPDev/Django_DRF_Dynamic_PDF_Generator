from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from .helpers import pdf_generator

# Create your views here.
class EmployeeListView(ListAPIView):
    """
    View to list employees
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeGeneratePdfAPIView(APIView):
    """
    View to generate PDF from employee records
    """
    def get(self, request):
        emp_objs = Employee.objects.all()
        context_dict = {
            'employees': emp_objs,
        }

        file_name, status =  pdf_generator(context_dict)

        if not status:
            return Response({
                'status': 400,
                'message': 'Something went wrong'
            })
        return Response({
            'status': status,
            'file_name': f'/media/{file_name}.pdf'
        })
