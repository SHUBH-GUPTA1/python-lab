# class Employee:
#     def __init__(self,name,employee_id,department,salary):
#         self.name=name
#         self.employee_id=employee_id
#         self.department=department
#         self.salary=salary
#     def increase_salary_by_department(self,department,percent_increase):
#         if self.department==department:
#             self.salary*=(1+percent_increase/100)
# no_of_employee=int(input("enter number of employee details you want"))
# employees=[]
# for i in range(no_of_employee):
#     print("enter",i,"th employee details")
#     print("enter employee name")
#     name=input()
#     print("enter employee id")
#     id=input()
#     print("enter employee department")
#     dept=input()
#     print("enter employee salary")        
#     sal=int(input())
#     employees.append(Employee(name,id,dept,sal))
#     print("emp name \t emp id \t emp dept \t emp sal")
#     for emp in employees:
#         print(emp.name, '\t' ,emp.employee_id,'\t',emp.department,'\t',emp.salary)
# dept=input("enter the department you want to increase salary")
# for Employee in employees:
#     if Employee.department==dept:
#         Employee.increase_salary_by_department(dept,10)
# for Employee in employees:
#     print(Employee.name,Employee.salary)        





class Employee:
    def __init__(self,name,employee_id,department,salary):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        self.salary=salary
    def increase_salary_by_department(self,department,percent_increase):
        if self.department==department:
            self.salary*=(1+percent_increase/100)    
no_of_employee=int(input("enter the number of employee details"))        
employees=[]
for i in range(no_of_employee):
    print("enter",i,"th employee details")
    print("enter employee name")
    name=input()
    print("enter employee id")
    id=input()
    print("enter employee department")
    dept=input()
    print("enter employee salary")
    sal=int(input())
    employees.append(Employee(name,id,dept,sal))
print("emp name \t emp id \t emp dept \t emp sal \n")
for emp in employees:
    print(emp.name,'\t',emp.employee_id,'\t',emp.department,'\t',emp.salary,'\n')
dept=input("enter the department you want to increase salary")
for Employee in employees:
    if Employee.department==dept:
        Employee.increase_salary_by_department(dept,10)
for Employee in employees:
    print(Employee.name,Employee.salary)