from django.contrib import admin
from django.conf.locale.en import formats as en_formats

from .models import Staff, Patients


# Register your models here.

# changes time represenation in django admin model panel same as 'strftime('H:M')'
en_formats.TIME_FORMAT = 'H:i'


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'speciality', 'work_time', 'days_off']
    

class StaffAppointmetnsAdmin(admin.ModelAdmin):
    list_display = ['staff_member', 'date_appointment', 'time_appointment', 'name']
    search_fields = ['staff_member__name', ]


admin.site.register(Staff, StaffAdmin)
admin.site.register(Patients, StaffAppointmetnsAdmin)