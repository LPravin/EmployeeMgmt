from django.urls import path
from task.views import *

urlpatterns = [
    path('', index),
    path('home/', log, name='login'),
    path('log/', home, name='home'),
    path('emp/', emppage),
    path('creemp/', creemp),
    path('manager-signup/', ManagerSignup, name="manager signup"),
    path('employee-signup/', EmployeeSignup, name="employee signup"),
    path('manage-employees/', manageEmployees, name="manage employees"),
    path('profile/', manageEmployees, name="profile"),
    path('add-skills/', addskill, name="add skill"),
    path('add-skills/ajax/load-skills/', load_skills, name="load skill"),
    path('add-skills/ajax/add-skill/', add_skill, name="submit skill"),
    path('add-skills/edit-skill/<int:pk>', edit_skill, name='edit skill'),
    path('add-skills/delete-skill/<int:pk>', delete_skill, name='delete skill'),
    path('logout/', userlogout, name='logout'),
    # path('manage-employees/update-employee/<str:pk>', update_employee, name="update employee"),
    path('manage-employees/delete-employee/<str:pk>', delete_employee, name="delete employee"),
    path('manage-employees/view-skill/<str:pk>', manageSkill, name="view skills"),
    # path('add-skills/ajax/update-skill',)
    # path('add-skills/ajax/update-skill',)
]
