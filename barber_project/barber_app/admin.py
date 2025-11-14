from django.contrib import admin
from .models import Client, Barber, Service, BarberService, Schedule, Visit, Review
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    list_per_page = 20

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'rating', 'is_active']
    list_filter = ['is_active']
    search_fields = ['first_name', 'last_name']
    list_per_page = 20

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    list_per_page = 20

@admin.register(BarberService)
class BarberServiceAdmin(admin.ModelAdmin):
    list_display = ['barber', 'service']
    list_filter = ['barber', 'service']
    list_per_page = 20

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['barber', 'day_of_week', 'start_time', 'end_time']
    list_filter = ['barber', 'day_of_week']
    list_per_page = 20

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['client', 'barber_service', 'visit_date', 'start_time', 'status', 'total_price']
    list_filter = ['status', 'visit_date', 'barber_service__barber']
    search_fields = ['client__first_name', 'client__last_name']
    list_per_page = 20
    date_hierarchy = 'visit_date'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['visit', 'rating', 'created_date']
    list_filter = ['rating', 'created_date']
    search_fields = ['visit__client__first_name', 'visit__client__last_name']
    list_per_page = 20
    date_hierarchy = 'created_date'