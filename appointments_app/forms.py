import datetime

from django import forms
from django.forms import ModelChoiceField
from django.forms.extras.widgets import SelectDateWidget

from .models import (Staff, Patients,
                     STAFF_WORK_TIME_DEFAULT, STAFF_DAYS_OFF_DEFAULT
                     )




MONTHS_RU = { 1: ('Январь'), 2: ('Февраль'), 3: ('Март'),
              4: ('Апрель'), 5: ('Май'), 6: ('Июнь'),
              7: ('Июль'), 8: ('Август'), 9: ('Сентябрь'),
             10: ('Октябрь'), 11: ('Ноябрь'), 12: ('Декабрь')
             }
DAYS_NAMES_RU = {'Saturday': 'Суббота',
                   'Sunday': 'Воскресение'
                 }
DATEFIELD_ERROR_MESSAGE_DEFAULT = {'invalid': 'Выбранной даты не существует'
                                   }


class AppointmentsForm(forms.ModelForm):
    # form fields block
    staff_member = ModelChoiceField(queryset=Staff.objects.all())
    date_appointment = forms.DateField(widget=SelectDateWidget(months=MONTHS_RU),
                                       initial=lambda: datetime.datetime.now(),
                                       error_messages=DATEFIELD_ERROR_MESSAGE_DEFAULT
                                       )
    time_appointment = forms.TimeField(widget=forms.TimeInput(format='%H:%M'),
                                       initial=lambda: datetime.datetime.now().strftime('%H:%M')
                                       )
    ## these fields have no model bindings,  after form post and before database saving processed into one value.
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    patronymic_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))

    class Meta:
        model = Patients
        fields = ('staff_member',
                  'date_appointment', 'time_appointment',
                  'first_name', 'patronymic_name', 'last_name')

    # form validation block
    def clean_staff_member(self):
        staff_member_choice = self.cleaned_data.get('staff_member', None)
        #if staff_member_choice.id != 4:
            #raise forms.ValidationError('Доступен только: {}'.format(Staff.objects.get(id=4).name))
        return staff_member_choice

    def clean_date_appointment(self):
        date_value_choice = self.cleaned_data.get('date_appointment', None)
        day_name_choice = str(date_value_choice.strftime("%A"))

        if day_name_choice in STAFF_DAYS_OFF_DEFAULT:
            raise forms.ValidationError(
                         'Выбранная дата приходится на нерабочий день: {}'.format(DAYS_NAMES_RU[day_name_choice])
                         )
        return date_value_choice

    def clean_time_appointment(self):
        # gets chosen date
        date_value_choice = self.cleaned_data.get('date_appointment', None)
        if not date_value_choice:
            raise forms.ValidationError('Для определения доступного времени необходимо указать корректную дату.')

        # gets chosen staff member id
        staff_member_choice = self.cleaned_data.get('staff_member', None)
        if not staff_member_choice:
            raise forms.ValidationError('Для определения доступного времени необходимо сделать выбор из предложенных врачей.')
        else:
            staff_member_choice_id = staff_member_choice.id

        # checks chosen time against work time and busy time
        staff_member_choice_BUSY_time = Patients.objects.filter(date_appointment=date_value_choice,
                                                                staff_member=staff_member_choice_id
                                                                )
        staff_member_choice_BUSY_time = [obj.time_appointment for obj in staff_member_choice_BUSY_time]
        staff_member_choice_FREE_time = ', '.join(
            [t.strftime('%H:%M') for t in STAFF_WORK_TIME_DEFAULT if t not in staff_member_choice_BUSY_time]
            )
        time_value_post = self.cleaned_data.get('time_appointment', None)
        time_value_post = time_value_post.strftime('%H:%M')

        if time_value_post not in staff_member_choice_FREE_time and staff_member_choice_FREE_time:
            raise forms.ValidationError('Выберите доступное время из списка: {}'.format(staff_member_choice_FREE_time))
        elif not staff_member_choice_FREE_time:
            raise forms.ValidationError('На данную дату у выбранного врача нет свободного времени. Выберите другую дату или другого врача.')

        return time_value_post