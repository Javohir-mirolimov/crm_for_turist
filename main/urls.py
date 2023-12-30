from django.urls import path
from .views import *

urlpatterns = [

    #------------Start Get Model------------------
    path('get-hotel/', GetHotel ),
    path('get-room/', GetRoom ),
    path('get-order-room/', GetOrder_room ),
    path('get-achievement/', GetAchievement ),
    path('get-order-porkofka/', GetOrder_porkofka ),
    path('get-git/', GetGit ),
    path('get-order-restaran-food/', GetOrder_restaran_food ),
    path('get-employee/', GetEmployee ),
    path('get-restaran/', GetRestaran ),
    path('get-table/', GetTable ),
    path('get-restaran_room/', GetRestaran_room ),
    path('get-order/', GetOrder ),
    path('get-employee-restaran/', GetEmployee_restaran ),
    path('get-menu/', GetMenu ),
    path('get-category/', GetCategory ),
    path('get-sub_category/', GetSub_category ),
    path('get-sub_category/', GetSub_category ),
    path('get-otel_food/', GetHotel_food ),
    path('get-order_hotel_food/', GetOrder_hotel_food ),
    #-------------Start Slug Model--------------------
    path('room-api/<slug:slug>/', room_api),
    path('hotel-food-api/<slug:slug>/', hotel_food_api),
    path('porkafka-api/<slug:slug>/', porkafka_api),
    path('git-api/<slug:slug>/', git_api),
    path('table-api/<slug:slug>/', table_api),
    path('restaran-room-api/<slug:slug>/', restaran_room_api),
    path('restaran-api/<slug:slug>/', restaran_api),
    path('hotel-api/<slug:slug>/', hotel_api),
    #---------------Start Filter Model----------------------
    path('filter-hotel-by-name/', filter_hotel_by_name),
    path('filter-hotel-by-rating/', filter_hotel_by_rating),
    path('filter-hotel-by-sub-category-address/<int:pk>/', filter_hotel_by_sub_category_address),
    path('filter-sub-category-address-by-category-address/<int:pk>/', filter_sub_category_address_by_category_address),
    path('filter-hotel-room-by-name/', filter_hotel_room_by_name),
    path('filter-hotel-room-by-is-delivery/', filter_hotel_room_by_is_delivery),
    path('filter-hotel-room-by-people-number/', filter_hotel_room_by_people_number),
    path('filte-hotel-room-by-status/', filter_hotel_room_by_status),
    path('filter-hotel-room-by-luks/', filter_hotel_room_by_luks),
    path('filter-achievement-by-name/', filter_achievement_by_name),
    path('filter-restaran-by-name/', filter_restaran_by_name),
    path('filter-restaran-by-name/', filter_restaran_by_name),
    path('filter-git-by-user/', filter_git_by_user),
    path('filter-git-by-hotel/', filter_git_by_hotel),
    path('filter-git-experience/', filter_git_experience),
    path('filter-restaran-by-rating/', filter_restaran_by_rating),
    path('filter-restaran-by-address/', filter_restaran_by_address),
    path('filter-table-by-restaran/', filter_table_by_restaran),
    path('filter-table-by-is-delivery/', filter_table_by_is_delivery),
    path('filter-room-by-is-delivery/', filter_room_by_is_delivery),
    path('filter-room-by-restaran/', filter_room_by_restaran),
    path('filter-maen-by-sub-category/<int:pk>/', filter_maen_by_sub_category),
    path('filter-sub-category-by-category/<int:pk>/', filter_sub_category_by_category),
    path('filter-mean-by-is-sale/', filter_mean_by_is_sale),
    path('filter-mean-by-rating/', filter_mean_by_rating),
    path('filter-mean-by-price/', filter_mean_by_price),
    path('filter-hotel-food-by-price/', filter_hotel_food_by_price),





]