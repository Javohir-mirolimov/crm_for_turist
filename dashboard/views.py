from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from main.models import *
from main.serializers import *


""" Start CRUD Hotel"""

class CreateHotel(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializres


class UpdateHotel(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializres


class DeleteHotel(DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializres

""" End CRUD Hotel"""
class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializres


class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializres


class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializres



""" Start CRUD Order_Room"""
class CreateOrder_Room(ListCreateAPIView):
    queryset = Order_room.objects.all()
    serializer_class = Order_roomSerializres


class UpdateOrder_Room(UpdateAPIView):
    queryset = Order_room.objects.all()
    serializer_class = Order_roomSerializres


class DeleteOrder_Room(DestroyAPIView):
    queryset = Order_room.objects.all()
    serializer_class = Order_roomSerializres

""" End CRUD OrderRroom"""

""" Start CRUD Hotel_food"""

class CreateHotel_Food(ListCreateAPIView):
    queryset = Hotel_food.objects.all()
    serializer_class = Hotel_foodSerializres

class UpdateHotel_Food(UpdateAPIView):
    queryset = Hotel_food.objects.all()
    serializer_class = Hotel_foodSerializres

class DeleteHotel_Food(DestroyAPIView):
    queryset = Hotel_food.objects.all()
    serializer_class = Hotel_foodSerializres

""" End CRUD Hotel_food"""

""" Start CRUD Order_Hotel_food"""

class CreateOrder_Hotel_Food(ListCreateAPIView):
    queryset = Order_hotel_food.objects.all()
    serializer_class = Order_hotel_foodSerializres

class UpdateOrder_Hotel_Food(UpdateAPIView):
    queryset = Order_hotel_food.objects.all()
    serializer_class = Order_hotel_foodSerializres

class DeleteOrder_Hotel_Food(DestroyAPIView):
    queryset = Order_hotel_food.objects.all()
    serializer_class = Order_hotel_foodSerializres

""" End CRUD Order_Hotel_food"""

""" Start  CRUD Porkofka """

class CreatePorkofka(ListCreateAPIView):
    queryset = Porkofka.objects.all()
    serializer_class = PorkofkaSerializres

class UpdatePorkofka(UpdateAPIView):
    queryset = Porkofka.objects.all()
    serializer_class = PorkofkaSerializres

class DeletePorkofka(DestroyAPIView):
    queryset = Porkofka.objects.all()
    serializer_class = PorkofkaSerializres

""" End  CRUD Porkofka """

""" Start CRUD Achievement """
class CreateAchievement(ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializres

class UpdateAchievement(UpdateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializres

class DeleteAchievement(DestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializres

""" End CRUD Achievement """

""" Start CRUD Order_porkofka"""
class CreateOrder_porkofka(ListCreateAPIView):
    queryset = Order_porkofka.objects.all()
    serializer_class = Order_porkofkarSerializres

class UpdateOrder_porkofka(UpdateAPIView):
    queryset = Order_porkofka.objects.all()
    serializer_class = Order_porkofkarSerializres

class DeleteOrder_porkofka(DestroyAPIView):
    queryset = Order_porkofka.objects.all()
    serializer_class = Order_porkofkarSerializres

""" End CRUD Order_porkofka"""

""" Start CURD Git"""
class CreateGit(ListCreateAPIView):
    queryset = Git.objects.all()
    serializer_class = GitSerializres

class UpdateGit(UpdateAPIView):
    queryset = Git.objects.all()
    serializer_class = GitSerializres

class DeleteGit(DestroyAPIView):
    queryset = Git.objects.all()
    serializer_class = GitSerializres

""" End CURD Git"""

""" Start CURD Order_Restaran_Food"""
class Createorder_restaran_food(ListCreateAPIView):
    queryset = Order_restaran_food.objects.all()
    serializer_class = Order_restaran_foodSerializres

class Updateorder_restaran_food(UpdateAPIView):
    queryset = Order_restaran_food.objects.all()
    serializer_class = Order_restaran_foodSerializres

class Deleteorder_restaran_food(DestroyAPIView):
    queryset = Order_restaran_food.objects.all()
    serializer_class = Order_restaran_foodSerializres

""" End CURD Order_Restaran_Food"""

""" Start CURD Employee """
class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializres

class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializres

class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializres

""" End CURD Employee """

""" Start CURD Restaran"""

class CreateRestaran(ListCreateAPIView):
    queryset = Restaran.objects.all()
    serializer_class = RestaranSerializres

class UpdateRestaran(UpdateAPIView):
    queryset = Restaran.objects.all()
    serializer_class = RestaranSerializres

class DeleteRestaran(DestroyAPIView):
    queryset = Restaran.objects.all()
    serializer_class = RestaranSerializres

""" End CURD Restaran"""

""" Start CURD Table"""

class CreateTable(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializres


class UpdateTable(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializres


class DeleteTable(DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializres

""" End CURD Table"""

""" Start Curd Restaran_room"""

class CreateRestaran_room(ListCreateAPIView):
    queryset = Restaran_room.objects.all()
    serializer_class = Restaran_roomSerializres

class UpdateRestaran_room(UpdateAPIView):
    queryset = Restaran_room.objects.all()
    serializer_class = Restaran_roomSerializres

class DeleteRestaran_room(DestroyAPIView):
    queryset = Restaran_room.objects.all()
    serializer_class = Restaran_roomSerializres

""" End Curd Restaran_room"""

""" Start Curd Order"""

class CreateOrder(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializres

class UpdateOrder(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializres

class DeleteOrder(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializres

""" End Curd Order"""

""" Start CURD Restaran_employee"""

class CreateRestaran_employee(ListCreateAPIView):
    queryset = Employee_restaran.objects.all()
    serializer_class = Employee_restaranSerializres

class UpdateRestaran_employee(UpdateAPIView):
    queryset = Employee_restaran.objects.all()
    serializer_class = Employee_restaranSerializres

class DeleteRestaran_employee(DestroyAPIView):
    queryset = Employee_restaran.objects.all()
    serializer_class = Employee_restaranSerializres

""" End CURD Restaran_employee"""

""" Start CURD Menu"""

class CreateMenu(ListCreateAPIView):
    queryset = Mean.objects.all()
    serializer_class = MeanSerializres


class UpdateMenu(UpdateAPIView):
    queryset = Mean.objects.all()
    serializer_class = MeanSerializres


class DeleteMenu(DestroyAPIView):
    queryset = Mean.objects.all()
    serializer_class = MeanSerializres

""" End CURD Menu"""