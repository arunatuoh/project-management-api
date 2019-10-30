from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Employee, Project, Empolyee_to_project
from django.db import IntegrityError
from rest_framework import status


@csrf_exempt
def add_new_employee(request):
    """

    :param request:
    :return:
    """

    try:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            emp_num = request.POST["emp_num"]
            last_name = request.POST["last_name"]
            sex = request.POST["gender"]
            role = request.POST["role"]
            emp_obj = Employee(emp_num=emp_num, first_name=first_name, last_name=last_name, sex=sex, role=role)
            emp_obj.save()
            return JsonResponse({"message": "Employee is created", "status": status.HTTP_201_CREATED})
        else:
            return JsonResponse({"message": "Method not allowed", "status": status.HTTP_405_METHOD_NOT_ALLOWED})
    except IntegrityError as ie:
        print("integrity error:", ie)
    except Exception as e:
        print("error is: ", e)
    return JsonResponse({"message": "Employee is not created", "status": status.HTTP_417_EXPECTATION_FAILED})


@csrf_exempt
def add_new_project(request):
    """

    :param request:
    :return:
    """

    try:
        if request.method == "POST":
            project_no = request.POST["project_no"]
            project_name = request.POST["project_name"]
            dept_no = request.POST["dept_no"]
            manager = request.POST["manager_id"]
            proj_st_date = request.POST["proj_st_date"]
            proj_en_date = request.POST["proj_en_date"]
            manager_instance = Employee.objects.get(emp_num=manager)

            project_obj = Project(project_no=project_no, project_name=project_name,
                                  dept_no=dept_no, manager=manager_instance, proj_st_date=proj_st_date,
                                  proj_en_date=proj_en_date
                                  )
            project_obj.save()
            return JsonResponse({"message": "Project is created", "status": status.HTTP_201_CREATED})
        else:
            return JsonResponse({"message": "Method not allowed", "status": status.HTTP_405_METHOD_NOT_ALLOWED})

    except IntegrityError as ie:
        print("integrity error:", ie)
    except Exception as e:
        print("error is: ", e)
    return JsonResponse({"message": "Project is not created", "status": status.HTTP_417_EXPECTATION_FAILED})


@csrf_exempt
def add_new_employee_to_project(request):
    """

    :param request:
    :return:
    """
    try:
        if request.method == "POST":
            emp_num = request.POST["emp_num"]
            project_no = request.POST["project_no"]
            project_ins = Project.objects.get(project_no=project_no)
            emp_ins = Employee.objects.get(emp_num=emp_num)
            emp_to_project_obj = Empolyee_to_project(employee=emp_ins, project=project_ins)
            emp_to_project_obj.save()
            return JsonResponse({"message": "Employee has been added to the project", "status": status.HTTP_200_OK})
        else:
            return JsonResponse({"message": "Method not allowed", "status": status.HTTP_405_METHOD_NOT_ALLOWED})
    except Exception as e:
        print(str(e))
    return JsonResponse({
        "message": "Employee can not be added to the project",
        "status": status.HTTP_417_EXPECTATION_FAILED
    })


"""

we cannot add a project without project manager's reference
"""
