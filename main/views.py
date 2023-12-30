from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

""" Start Get"""

@api_view(['GET'])
def GetHotel(request):
    hotel = Hotel.objects.all()
    ser = HotelSerializres(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetRoom(request):
    room = Room.objects.all()
    ser = RoomSerializres(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetOrder_room(request):
    order = Order_room.objects.all()
    ser = Order_roomSerializres(order, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetAchievement(request):
    achievement = Achievement.objects.all()
    ser = AchievementSerializres(achievement, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetOrder_porkofka(request):
    order = Order_porkofka.objects.all()
    ser = Order_porkofkarSerializres(order, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetGit(request):
    git = Git.objects.all()
    ser = GitSerializres(git, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetOrder_restaran_food(request):
    order = Order_restaran_food.objects.all()
    ser = Order_restaran_foodSerializres(order, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetEmployee(request):
    employee = Employee.objects.all()
    ser = EmployeeSerializres(employee, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetRestaran(request):
    restaran = Restaran.objects.all()
    ser = RestaranSerializres(restaran, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetTable(request):
    table = Table.objects.all()
    ser = TableSerializres(table, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetRestaran_room(request):
    restaran_room = Restaran_room.objects.all()
    ser = Restaran_roomSerializres(restaran_room, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetOrder(request):
    order = Order.objects.all()
    ser = OrderSerializres(order, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetEmployee_restaran(request):
    employee = Employee_restaran.objects.all()
    ser = Employee_restaranSerializres(employee, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetMenu(request):
    mean = Mean.objects.all()
    ser = MeanSerializres(mean, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetCategory(request):
    category = Category.objects.all()
    ser = CategorySerializres(category, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetSub_category(request):
    sub_category = Sub_category.objects.all()
    ser = Sub_categorySerializres(sub_category, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetHotel_food(request):
    hotel_food = Hotel_food.objects.all()
    ser = Hotel_foodSerializres(hotel_food, many=True)
    return Response(ser.data)



@api_view(['GET'])
def GetOrder_hotel_food(request):
    order_hotel_food = Order_hotel_food.objects.all()
    ser = Order_hotel_foodSerializres(order_hotel_food, many=True)
    return Response(ser.data)

""" End Get"""

""" Start slug"""
@api_view(["GET"])
def room_api(request, slug):
    room = Room.objects.get(slug = slug)
    ser = RoomSerializres(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def hotel_food_api(request, slug):
    hotel_food = Hotel_food.objects.get(slug = slug)
    ser = Hotel_foodSerializres(hotel_food, many=True)
    return Response(ser.data)




@api_view(["GET"])
def porkafka_api(request, slug):
    porkafka = Porkofka.objects.get(slug = slug)
    ser = PorkofkaSerializres(porkafka, many=True)
    return Response(ser.data)


@api_view(["GET"])
def git_api(request, slug):
    git = Git.objects.get(slug = slug)
    ser = GitSerializres(git, many=True)
    return Response(ser.data)


@api_view(["GET"])
def table_api(request, slug):
    table = Table.objects.get(slug = slug)
    ser = RoomSerializres(table, many=True)
    return Response(ser.data)


@api_view(["GET"])
def restaran_room_api(request, slug):
    restaran_room = Restaran_room.objects.get(slug = slug)
    ser = Restaran_roomSerializres(restaran_room, many=True)
    return Response(ser.data)




@api_view(["GET"])
def mean_api(request, slug):
    mean = Mean.objects.get(slug = slug)
    ser = MeanSerializres(mean, many=True)
    return Response(ser.data)



@api_view(["GET"])
def hotel_api(request, slug):
    hotel = Hotel.objects.get(slug = slug)
    ser = HotelSerializres(hotel, many=True)
    return Response(ser.data)

@api_view(["GET"])
def restaran_api(request, slug):
    restaran = Restaran.objects.get(slug = slug)
    ser = RestaranSerializres(restaran, many=True)
    return Response(ser.data)

""" End Slug """


""" Start Filter"""
@api_view(['GET'])
def filter_hotel_by_name(reqeust):
    name = reqeust.GET.get('name', )
    hotel = Hotel.objects.filter(name__icontains=name)
    ser = HotelSerializres(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_hotel_by_rating(request):
    hotel = Hotel.objects.all().order_by('-reting')[:10]
    ser = HotelSerializres(hotel, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_hotel_by_sub_category_address(request, pk):
    category_address = Sub_category_address.objects.get(pk=pk)
    hotel = Hotel.objects.filter(category_address=category_address)
    ser = HotelSerializres(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_hotel_room_by_name(reuest):
    name = reuest.GET.get('name')
    room = Room.objects.filter(name__icontains=name)
    ser = RoomSerializres(room, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_sub_category_address_by_category_address(request, pk):
    sub_category_address = Sub_category_address.objects.filter(category_address_id=pk)
    ser = Sub_categorySerializres(sub_category_address, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_hotel_room_by_is_delivery(reuqest):
    room = Room.objects.filter(is_delivery=True)
    ser = RoomSerializres(room, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_hotel_room_by_people_number(request):
    number_people = request.GET.get('number_people')
    room = Room.objects.filter(number_people=number_people)
    ser = RoomSerializres(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_hotel_room_by_status(request):
    lusk_room = request.GET.get('lusk_room')
    if lusk_room:
        rooms = Room.objects.filter(lusk_room__icontains=lusk_room)
        ser = RoomSerializres(rooms, many=True)
        return Response(ser.data)
    else:
        return Response({"error": "'query' parameter is required"}, status=400)

@api_view(['GET'])
def filter_hotel_room_by_luks(reuqest):
    room = Room.objects.filter(luks=True)
    ser = RoomSerializres(room, many=True)
    return Response(ser.data)



@api_view(['GET'])
def filter_achievement_by_name(request):
    name = request.GET.get('name')
    achievement = Achievement.objects.filter(name__icontains=name)
    ser = AchievementSerializres(achievement, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_restaran_by_name(reqeust):
    name = reqeust.GET.get('name')
    restaran = Restaran.objects.filter(name__icotains=name)
    ser = RestaranSerializres(restaran, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_git_by_user(request):
    user = request.GET.get('user')
    git = Git.objects.filter(user_id=user)
    ser = GitSerializres(git, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_git_by_hotel(request):
    hotel = request.GET.get('hotel')
    git = Git.objects.filter(hotel_id=hotel)
    ser = GitSerializres(git, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_git_experience(request):
    experience = request.GET.get('experience')
    git = Git.objects.filter(experience=experience)
    ser = GitSerializres(git, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_restaran_by_rating(request):
    restaran = Restaran.objects.all().order_by('-reting')[:10]
    ser = RoomSerializres(restaran, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_restaran_by_address(request):
    address = request.GET.get('address')
    restaran = Restaran.objects.filter(address__icontains=address)
    ser = RestaranSerializres(restaran, many=True)
    return Response(ser.data)



@api_view(['GET'])
def filter_table_by_restaran(request):
    restaran = request.GET.get('restaran')
    table = Table.objects.filter(restaran_id=restaran)
    ser = TableSerializres(table, many=True)
    return Response(ser.data)



@api_view(['GET'])
def filter_table_by_is_delivery(reuqest):
    table = Table.objects.filter(is_delivery=True)
    ser = TableSerializres(table, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_restaran(request):
    restaran = request.GET.get('restaran')
    room = Restaran_room.objects.filter(restaran_id=restaran)
    ser = Restaran_roomSerializres(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_is_delivery(reuqest):
    room = Restaran_room.objects.filter(is_delivery=True)
    ser = Restaran_roomSerializres(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_maen_by_sub_category(request, pk):
    category = Sub_category.objects.get(pk=pk)
    mean = Mean.objects.filter(category=category)
    ser = MeanSerializres(mean, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_sub_category_by_category(request, pk):
    sub_category = Sub_category.objects.filter(category_id=pk)
    ser = Sub_categorySerializres(sub_category, many=True)
    return Response(ser.data)



@api_view(['GET'])
def filter_mean_by_is_sale(reuqest):
    mean = Mean.objects.filter(is_sale=True)
    ser = MeanSerializres(mean, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_mean_by_rating(request):
    mean = Mean.objects.all().order_by('-reting')[:10]
    ser = MeanSerializres(mean, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_mean_by_price(request):
    start_price = request.GET.get('s_price')
    end_price = request.GET.get('e_price')
    mean = Mean.objects.filter(price__gte=start_price, price__lte=end_price)
    ser = MeanSerializres(mean, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_hotel_food_by_price(request):
    start_price = request.GET.get('s_price')
    end_price = request.GET.get('e_price')
    food = Hotel_food.objects.filter(price__gte=start_price, price__lte=end_price)
    ser = Hotel_foodSerializres(food, many=True)
    return Response(ser.data)



    """ End Filter"""