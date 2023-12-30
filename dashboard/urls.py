from django.urls import path
from .views import *

urlpatterns = [
    #-------------------Start Crud Hotel Model------------------------
    path('create-hotel/',  CreateHotel.as_view()),
    path('update-hotel/<int:pk>/',  UpdateHotel.as_view()),
    path('delete-hotel/<int:pk>/',  DeleteHotel.as_view()),
    #-----------------Start Crud Room Model----------------------------
    path('create-room/', CreateRoom.as_view()),
    path('update-room/<int:pk>/', UpdateRoom.as_view()),
    path('delete-room/<int:pk>/', DeleteRoom.as_view()),
    #-----------------Start Crud Order_Room Model----------------------
    path('create-order-room/', CreateOrder_Room.as_view()),
    path('update-order-room/<int:pk>/', UpdateOrder_Room.as_view()),
    path('delete-order-room/<int:pk>/', DeleteOrder_Room.as_view()),
    #-------------------Start Crud Achievement Model--------------------
    path('create-achievement/', CreateAchievement.as_view()),
    path('update-achievement/<int:pk>/', UpdateAchievement.as_view()),
    path('delete-achievement/<int:pk>/', DeleteAchievement.as_view()),
    #------------------Start Curd Order_porkofka Model------------------
    path('create-order_porkofka/', CreateOrder_porkofka.as_view()),
    path('update-order_porkofka/<int:pk>/', UpdateOrder_porkofka.as_view()),
    path('delete-order_porkofka/<int:pk>/', DeleteOrder_porkofka.as_view()),
    #-------------------Start Curd GIt Model------------------------------
    path('create-git/', CreateGit.as_view()),
    path('update-git/<int:pk>/', UpdateGit.as_view()),
    path('delete-git/<int:pk>/', DeleteGit.as_view()),
    #--------------------Start Curd Order_restaran_food Model-------------------
    path('create-order-restaran-food/', Createorder_restaran_food.as_view()),
    path('update-order-restaran-food/<int:pk>/', Updateorder_restaran_food.as_view()),
    path('delete-order-restaran-food/<int:pk>/', Deleteorder_restaran_food.as_view()),
    #--------------------Start Curd Employeee Model-----------------------------
    path('create-employee/', CreateEmployee.as_view()),
    path('update-employee/<int:pk>/', UpdateEmployee.as_view()),
    path('delete-employee/<int:pk>/', UpdateEmployee.as_view()),
    #--------------------Start Curd Restaran Model--------------------------
    path('create-restaran/', CreateRestaran.as_view()),
    path('update-restaran/<int:pk>/', UpdateRestaran.as_view()),
    path('delete-restaran/<int:pk>/', DeleteRestaran.as_view()),
    #---------------------Start Crud Table Model----------------------------
    path('create-table/', CreateTable.as_view()),
    path('update-table/<int:pk>/', UpdateTable.as_view()),
    path('delete-table/<int:pk>/', DeleteTable.as_view()),
    #----------------------Start Curd Restaran_room Model-------------------
    path('create-restaran-room/', CreateRestaran_room.as_view()),
    path('update-restaram-room/<int:pk>/', UpdateRestaran_room.as_view()),
    path('delete-restaram-room/<int:pk>/', DeleteRestaran_room.as_view()),
    #-----------------------Start Curd Order Model-------------------------
    path('create-order/', CreateOrder.as_view()),
    path('update-order/<int:pk>/', UpdateOrder.as_view()),
    path('delete-order/<int:pk>/', DeleteOrder.as_view()),
    #-----------------------Start Curd Employee_Restaran Model--------------
    path('create-employee-restaran/', CreateRestaran_employee.as_view()),
    path('update-employee-restaran/<int:pk>/', UpdateRestaran_employee.as_view()),
    path('dalete-employee-restaran/<int:pk>/', DeleteRestaran_employee.as_view()),
    #------------------------Start Crud Menu Model--------------------------
    path('create-menu/', CreateMenu.as_view()),
    path('update-menu/<int:pk>/', UpdateMenu.as_view()),
    path('delete-menu/<int:pk>/', DeleteMenu.as_view()),
    #-------------------------Start Crud Hotel_Food Model-------------------
    path('create-hotel-food', CreateHotel_Food.as_view()),
    path('update-hotel-food/<int:pk>/', UpdateHotel_Food.as_view()),
    path('delete-hotel-food/<int:pk>/', DeleteHotel_Food.as_view()),
    #--------------------------Start Crud Hotel Food Order Model--------------
    path('create-order-hotel-food/', CreateOrder_Hotel_Food.as_view()),
    path('update-order-hotel-food/<int:pk>/', UpdateOrder_Hotel_Food.as_view()),
    path('delete-order-hotel-food/<int:pk>/', DeleteOrder_Hotel_Food.as_view()),
]