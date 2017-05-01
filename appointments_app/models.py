import datetime

from django.db import models



# Create your models here.
STAFF_WORK_TIME_DEFAULT = [datetime.time(t, 0) for t in range(9, 18)]
STAFF_WORK_TIME_DEFAULT_db_ready = ', '.join(t.strftime('%H:%M:%S') for t in STAFF_WORK_TIME_DEFAULT)

STAFF_DAYS_OFF_DEFAULT = ['Saturday', 'Sunday']
STAFF_DAYS_OFF_DEFAULT_db_ready = ', '.join(STAFF_DAYS_OFF_DEFAULT)


class Staff(models.Model):
    speciality = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255, default=STAFF_WORK_TIME_DEFAULT_db_ready)
    days_off = models.CharField(max_length=255, default=STAFF_DAYS_OFF_DEFAULT_db_ready)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


class Patients(models.Model):
    staff_member = models.ForeignKey(Staff)
    date_appointment = models.DateField()
    time_appointment = models.TimeField()
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Запись на прием к врачу'
        verbose_name_plural = 'Записи на прием к врачам'