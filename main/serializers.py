from rest_framework import serializers
from .models import *




class UserSerializres(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class SponpersSerializres(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = "__all__"


class HotelSerializres(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class RoomSerializres(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class Order_roomSerializres(serializers.ModelSerializer):
    class Meta:
        model = Order_room
        fields = "__all__"

class PorkofkaSerializres(serializers.ModelSerializer):
    class Meta:
        model = Porkofka
        fields = "__all__"

class Hotel_foodSerializres(serializers.ModelSerializer):
    class Meta:
        model = Hotel_food
        fields = "__all__"


class Order_hotel_foodSerializres(serializers.ModelSerializer):
    class Meta:
        model = Porkofka
        fields = "__all__"
class AchievementSerializres(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"


class Order_porkofkarSerializres(serializers.ModelSerializer):
    class Meta:
        model = Order_porkofka
        fields = "__all__"


class GitSerializres(serializers.ModelSerializer):
    class Meta:
        model = Git
        fields = "__all__"


class Order_restaran_foodSerializres(serializers.ModelSerializer):
    class Meta:
        model = Order_restaran_food
        fields = "__all__"


class EmployeeSerializres(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class RestaranSerializres(serializers.ModelSerializer):
    class Meta:
        model = Restaran
        fields = "__all__"


class TableSerializres(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class Restaran_roomSerializres(serializers.ModelSerializer):
    class Meta:
        model = Restaran_room
        fields = "__all__"


class OrderSerializres(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class Employee_restaranSerializres(serializers.ModelSerializer):
    class Meta:
        model = Employee_restaran
        fields = "__all__"


class MeanSerializres(serializers.ModelSerializer):
    class Meta:
        model = Mean
        fields = "__all__"


class CategorySerializres(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Sub_categorySerializres(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = "__all__"

