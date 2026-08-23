from django.core.management.base import BaseCommand
from employee.models import Employee,Department


class Command(BaseCommand):
    help = "ORM Practice"
    def handle(self, *args, **kwargs):
        self.basic_queries()
    def basic_queries(self):
        print("============= 1.Aggregate Function(Max,Min,Avg,Sum,Count) =============")
        from django.db.models import Count,Max,Min,Avg,Sum
        print("=="*100)
        # 1.Count
        total_count=Department.objects.aggregate(Count('id'))
        # Also We can write like alias
        total_count_dept=Department.objects.aggregate(Total_count=Count("id"))
        print("Total_count",total_count_dept,type(total_count_dept))
        total_count_row=Department.objects.count()
        print(total_count_row)
        # 2.Max
        max_salary=Employee.objects.aggregate(max_salary=Max('salary'))
        print("Max Salary",max_salary)
        # 3.Min
        min_salary=Employee.objects.aggregate(min_salary=Min('salary'))
        print(min_salary)
        # 4.Avg
        avg_salary=Employee.objects.aggregate(avg_salary=Avg('salary'))
        print("Average salary===>",avg_salary)
        # 5.Sum
        sum_salary=Employee.objects.aggregate(sum_salary=Sum('salary'))
        print("sum of salary===>",sum_salary)

        print("============= 2.Annotate Function =============")
        # Show every department with the total number of employees.
        total_number_employee=Department.objects.annotate(total_employee_count=Count('employee')).values()
        print("Total Number Of Employee",list(total_number_employee))
        for i in total_number_employee:
            print(i)
        # Show every department with the average employee salary.
        avg_salary_all_employee=Department.objects.annotate(avg_salary=Avg("employee__salary")).values()
        print(avg_salary_all_employee)
        # Show every department with the highest salary.
        high_salary=Department.objects.annotate(high_salary=Max("employee__salary")).values()
        print("High Salary",high_salary)
        # Show every department with the lowest salary.
        lowest_sal=Department.objects.annotate(lowest_sal=Min("employee__salary")).values()
        # Show every department with the total salary.
        total_sal=Department.objects.annotate(total_sal=Sum("employee__salary")).values()
        print(total_sal)
        # Show only those departments that have more than 5 employees.
        dept=Department.objects.annotate(total_count=Count('employee')).filter(employee__gt=5).values()
        print(dept)
        dept_avg_sal=Department.objects.annotate(avg_sal=Avg('employee__salary')).filter(avg_sal__gt=50000).values()
        print("Average Salary",dept_avg_sal)